import re

# Old and new :root blocks
old_root = '''    :root {
      --bg:      oklch(96% 0.003 240);
      --surface: oklch(100% 0 0);
      --fg:      oklch(15% 0.01 240);
      --muted:   oklch(45% 0.01 240);
      --border:  oklch(88% 0.004 240);
      --accent:  oklch(42% 0.14 232);
      --accent-soft: oklch(94% 0.02 232);

      --font-display: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
      --font-body:    -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
      --font-mono:    ui-monospace, 'Segoe UI Mono', Menlo, monospace;
    }'''

new_root = '''    :root {
      /* Duolingo Design System — Owl Green + Chunky Shadows */
      --bg: #ffffff;
      --surface: #f7f7f7;
      --fg: #3c3c3c;
      --muted: #777777;
      --border: #e5e5e5;
      --accent: #58cc02;
      --accent-on: #ffffff;
      --accent-hover: #89e219;
      --accent-active: #58a700;
      --accent-soft: #dbf8c5;
      --secondary: #ff9600;
      --success: #58cc02;
      --warn: #ffc800;
      --danger: #ff4b4b;

      --font-display: "Feather Bold", "DIN Round Pro", "Helvetica Neue", sans-serif;
      --font-body: "Mona Sans", "Helvetica Neue", system-ui, sans-serif;
      --font-mono: "JetBrains Mono", ui-monospace, Menlo, Monaco, Consolas, monospace;
    }'''

# Typography updates
old_h_base = '''    h1, h2, h3, h4, h5, h6 {
      font-family: var(--font-display);
      font-weight: 600;
      line-height: 1.15;
      letter-spacing: -0.02em;
    }'''

new_h_base = '''    h1, h2, h3, h4, h5, h6 {
      font-family: var(--font-display);
      font-weight: 800;
      line-height: 1.15;
      letter-spacing: -0.01em;
    }'''

# Footer button old/new
old_footer_btn = '''    footer .back-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 20px;
      background: var(--accent);
      color: white;
      border-radius: 6px;
      font-weight: 510;
      font-size: 14px;
      transition: all 0.2s;
      text-decoration: none;
    }

    footer .back-btn:hover {
      background: oklch(38% 0.14 232);
      transform: translateX(-2px);
      opacity: 1;
    }'''

new_footer_btn = '''    footer .back-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 20px;
      background: var(--accent);
      color: var(--accent-on);
      border-bottom: 4px solid var(--accent-active);
      border-radius: 16px;
      font-family: var(--font-display);
      font-weight: 800;
      font-size: 14px;
      letter-spacing: 0.02em;
      transition: all 0.18s cubic-bezier(0.34, 1.56, 0.64, 1);
      text-decoration: none;
    }

    footer .back-btn:hover {
      background: var(--accent-hover);
      opacity: 1;
    }

    footer .back-btn:active {
      transform: translateY(2px);
      border-bottom-width: 2px;
    }'''

files = ['iff-case-study.html', 'sehrana-case-study.html', 'swfp-case-study.html', 'penfed-case-study.html', 'intel-case-study.html']

for filename in files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace :root block
        content = content.replace(old_root, new_root)
        
        # Replace h1-h6 base
        content = content.replace(old_h_base, new_h_base)
        
        # Replace footer button
        content = content.replace(old_footer_btn, new_footer_btn)
        
        # Update individual heading weight/letter-spacing
        content = re.sub(r'font-weight: 600;(\s*)letter-spacing: -0\.025em;', r'font-weight: 800;\1letter-spacing: -0.01em;', content)
        content = re.sub(r'font-weight: 600;(\s*)letter-spacing: -0\.02em;', r'font-weight: 800;\1letter-spacing: -0.01em;', content)
        content = re.sub(r'font-weight: 600;(\s*)letter-spacing: -0\.015em;', r'font-weight: 800;\1letter-spacing: normal;', content)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated {filename}")
    except Exception as e:
        print(f"Error updating {filename}: {e}")
