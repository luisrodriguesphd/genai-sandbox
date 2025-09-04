from slide_generator import SlideGenerator
import argparse
import json
import os
from typing import Dict

def validate_config(config: Dict, schema_path: str) -> bool:
    """
    Validate the configuration against the schema.
    
    Args:
        config (Dict): Configuration to validate
        schema_path (str): Path to the schema file
        
    Returns:
        bool: True if valid, raises ValueError if invalid
    """
    with open(schema_path, 'r') as f:
        schema = json.load(f)
    
    valid_templates = {slide['name'] for slide in schema['slides']}
    
    if 'sections' not in config:
        raise ValueError("Configuration must contain 'sections'")
        
    for section in config['sections']:
        if 'slides' not in section:
            raise ValueError(f"Section {section.get('name', 'unnamed')} must contain 'slides'")
            
        for slide in section['slides']:
            if 'template' not in slide:
                raise ValueError("Each slide must specify a template")
            if slide['template'] not in valid_templates:
                raise ValueError(f"Invalid template: {slide['template']}")
            
            # If content is provided, validate against schema
            if 'content' in slide:
                template_schema = next(t for t in schema['slides'] if t['name'] == slide['template'])
                required_fields = {
                    field_name for field_name, field in template_schema['fields'].items()
                    if field.get('required', False)
                }
                
                for field in required_fields:
                    if field not in slide['content']:
                        raise ValueError(f"Missing required field '{field}' in {slide['template']} slide")
    
    return True

def main():
    parser = argparse.ArgumentParser(description='Generate PowerPoint presentation from template')
    parser.add_argument('--template', required=True, help='Path to template PPTX file')
    parser.add_argument('--schema', required=True, help='Path to template schema JSON file')
    parser.add_argument('--config', required=True, help='Path to configuration JSON file')
    parser.add_argument('--output', required=True, help='Path for output PPTX file')
    
    args = parser.parse_args()
    
    # Validate paths
    for path in [args.template, args.schema, args.config]:
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")
    
    # Load and validate configuration
    with open(args.config, 'r') as f:
        config = json.load(f)
    
    validate_config(config, args.schema)
    
    # Generate presentation
    generator = SlideGenerator(args.template, args.schema)
    generator.generate_presentation(args.config, args.output)
    print(f"Presentation generated successfully: {args.output}")

if __name__ == '__main__':
    main()
