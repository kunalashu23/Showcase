#!/usr/bin/env python3
"""
Reorder portfolio sections following NN/g IA principles:
Hero → Research Approach → Featured Work → Recognition → Contact
Also fix color consistency in Recognition section.
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find section boundaries
research_approach_start = content.find('<!-- Research Approach (Concise) -->')
research_approach_end = content.find('  </section>', research_approach_start) + len('  </section>')

# Find where Featured Work section comment should be
featured_work_comment_pos = content.find('<!-- Featured Work -->')
if featured_work_comment_pos == -1:
    # It was changed, find the section tag instead
    featured_work_comment_pos = content.find('<section class="featured-work"')

# Find actual Featured Work content (currently mismatched)
featured_work_heading = content.find('<h2 id="work-heading">Featured Work</h2>')
if featured_work_heading == -1:
    print("ERROR: Could not find Featured Work heading")
    exit(1)

# Work backwards to find the section start
temp_pos = featured_work_heading
while temp_pos > 0 and '<section' not in content[temp_pos-100:temp_pos]:
    temp_pos -= 1

featured_work_actual_start = content.rfind('<section', 0, featured_work_heading)
featured_work_end = content.find('  </section>', featured_work_heading) + len('  </section>')

# Find Recognition content (currently mixed with Featured Work section tag)
recognition_heading = content.find('<h2>Recognition & Impact</h2>')
if recognition_heading == -1:
    print("ERROR: Could not find Recognition heading")
    exit(1)

# Find Recognition start (the section tag before the heading)
recognition_section_start = content.rfind('<section', 0, recognition_heading)
recognition_end = content.find('  </section>', recognition_heading) + len('  </section>')

print(f"Research Approach: {research_approach_start} to {research_approach_end}")
print(f"Recognition section: {recognition_section_start} to {recognition_end}")
print(f"Featured Work section: {featured_work_actual_start} to {featured_work_end}")

# Extract sections
research_approach_section = content[research_approach_start:research_approach_end]
recognition_section_content = content[recognition_section_start:recognition_end]
featured_work_section_content = content[featured_work_actual_start:featured_work_end]

# Build new order: Research Approach → Featured Work → Recognition
new_middle = (
    research_approach_section + '\n\n' +
    featured_work_section_content + '\n\n' +
    recognition_section_content
)

# Replace the middle section
new_content = (
    content[:research_approach_start] +
    new_middle +
    content[recognition_end:]
)

# Fix color consistency in Recognition section
# Change warm gradients to match the cool blue-green Material/Carbon system
new_content = new_content.replace(
    'background: linear-gradient(90deg, var(--warn) 0%, var(--secondary) 100%);',
    'background: linear-gradient(90deg, var(--accent) 0%, var(--success) 100%);'
)

# Fix the gradient icon badge colors in Recognition
new_content = new_content.replace(
    'background: linear-gradient(135deg, #f9ab00 0%, #ea4335 100%);',
    'background: linear-gradient(135deg, var(--accent) 0%, var(--success) 100%);'
)

# Write the fixed content
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✓ Sections reordered: Hero → Research Approach → Featured Work → Recognition → Contact")
print("✓ Color consistency fixed: Recognition now uses blue-green system")
