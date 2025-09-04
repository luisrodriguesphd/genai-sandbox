# Template-Based PowerPoint Generation

This project provides a Python-based solution for generating PowerPoint presentations from templates. It allows you to define slide templates and generate new presentations by reusing and combining these templates with different content.

## Features

- Template-based slide generation
- Support for multiple slide types (title, section, content, etc.)
- JSON-based configuration
- Schema validation for configurations
- Support for bullet points and text replacement
- Automatic template slide removal after generation

## Requirements

- Python 3.7+
- python-pptx
- python-docx

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
template-based-pptx-generation/
├── template.pptx          # Your template presentation
├── template_schema.json   # Schema defining available slide types
├── example_config.json    # Example configuration
├── main.py               # Main script
├── slide_generator.py    # Core generation logic
└── requirements.txt      # Python dependencies
```

## Template Schema

The `template_schema.json` file defines the available slide types and their fields. The slides in the schema should match the order of slides in your template.pptx file. Each slide type includes:

- `name`: Identifier for the slide type
- `goal`: Description of the slide's purpose
- `fields`: Required and optional fields for the slide

Available slide types (in order):

1. Title Slide (`title`):
```json
{
  "name": "title",
  "goal": "First slide of the presentation",
  "fields": {
    "title": {
      "description": "Main title of the presentation",
      "type": "text",
      "required": true
    },
    "subtitle": {
      "description": "Supporting subtitle text",
      "type": "text",
      "required": false
    }
  }
}
```

2. Section Slide (`section`):
```json
{
  "name": "section",
  "goal": "Introduce a new section or topic",
  "fields": {
    "section_title": {
      "description": "Title of the section",
      "type": "text",
      "required": true
    }
  }
}
```

3. Content Slide (`content_1`):
```json
{
  "name": "content_1",
  "goal": "Present detailed information with bullet points",
  "fields": {
    "title": {
      "description": "Slide title",
      "type": "text",
      "required": true
    },
    "bullet_points": {
      "description": "List of bullet points",
      "type": "array",
      "items": "text",
      "required": true
    }
  }
}
```

4. Thank You Slide (`thank_you`):
```json
{
  "name": "thank_you",
  "goal": "Final slide without any fields",
  "fields": {}
}
```

## Configuration Format

The configuration file specifies the structure and content of the generated presentation:

```json
{
  "sections": [
    {
      "name": "Section Name",
      "slides": [
        {
          "template": "content_1",
          "content": {
            "title": "Slide Title",
            "bullet_points": [
              "Point 1",
              "Point 2"
            ]
          }
        }
      ]
    }
  ]
}
```

## Template Preparation

### Creating template.pptx

1. Create a PowerPoint presentation with your template slides
2. Order slides to match the schema (in our example):
   - Slide 1: Title slide
   - Slide 2: Section slide
   - Slide 3: Content slide with bullet points
   - Slide 4: Thank you slide

### Placeholder Text Format

Each slide type requires specific placeholder text for content replacement:

1. Title Slide:
   ```
   {{ title }}      - For the main title
   {{ subtitle }}   - For the subtitle (optional)
   ```

2. Section Slide:
   ```
   {{ section_title }}  - For the section title
   ```

3. Content Slide (with bullet points):
   ```
   {{ title }}         - For the slide title
   {{ bullet_points }} - Where you want the bullet points to appear
   ```

4. Thank you slide:
   - No placeholders needed (static content)

### Important Notes:

- Placeholders must use exactly two curly braces on each side: `{{ like_this }}`
- The placeholder names must match the field names in your template_schema.json
- Place the bullet points placeholder (`{{ bullet_points }}`) in the text box where you want the bullet points to appear
- For bullet points, the entire placeholder will be replaced with the list of points
- Keep the original template.pptx as a backup before making changes

### Example Content Box Setup

For a content slide with bullet points:
```
{{ title }}

{{ bullet_points }}
```

When replaced, it will look like:
```
Key Development Practices

• Version Control with Git
• Continuous Integration/Deployment
• Test-Driven Development
• Code Reviews
```

## Usage

Run the script with your template, schema, and configuration:

```bash
python main.py --template template.pptx --schema template_schema.json --config your_config.json --output generated.pptx
```

## Example Configuration

An example configuration is provided in `example_config.json` that demonstrates how to create a complete presentation with multiple sections. The example creates a 7-slide presentation about software development:

### Presentation Structure

1. Introduction Section:
   - Title slide with main title "Modern Software Development" and subtitle

2. Development Process Section:
   - Section slide introducing "Development Workflow"
   - Content slide about "Key Development Practices"
   - Content slide covering "Code Quality Practices"

3. Best Practices Section:
   - Section slide for "Development Best Practices"
   - Content slide detailing "Code Quality Guidelines"

4. Conclusion:
   - Thank you slide

### Key Features Demonstrated

- Multiple sections with logical flow
- Reuse of slide templates (content_1 template used three times)
- Mix of different slide types (title, section, content, thank you)
- Both simple and complex slides (with and without bullet points)
- Proper content organization with section slides

### Example Usage

```bash
python main.py --template template.pptx --schema template_schema.json --config example_config.json --output generated.pptx
```

The configuration shows how to:
1. Structure your presentation into logical sections
2. Use section slides for clear topic transitions
3. Reuse slide templates with different content
4. Maintain consistent formatting across similar slides
5. Create a professional flow from introduction to conclusion

## LLM Integration

The template schema is designed to be LLM-friendly, allowing AI models to:
1. Understand available slide types and their purposes
2. Know required and optional fields for each slide type
3. Generate valid configurations based on the schema
4. Create presentations with appropriate content organization

## Error Handling

The system includes validation for:
- File existence checks
- Schema compliance
- Required field validation
- Template availability
- Configuration structure

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
