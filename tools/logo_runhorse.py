# Galloping horse silhouette, facing right (viewBox 0 -6 120 84). One flat color, built from overlapping shapes.
def run_horse(fill='currentColor'):
    return f'''<g fill="{fill}" stroke="{fill}" stroke-linecap="round" stroke-linejoin="round">
<path d="M27 27 C19 19 9 19 2 25 C8 26 12 28 14 32 C8 35 4 42 4 50 C11 42 20 38 29 35 Z" stroke-width="1"/>
<path d="M30 25 C40 21 58 23 68 22 C74 15 82 7 89 3 L93 1 C100 5 108 12 115 19 Q116 23 112 26 L109 26 C105 23 101 19 97.5 16.5 C94 25 89 36 85 42 C81 46 75 47 69 46 C57 48 45 48 37 45 C29 43 23 37 25 29 Z" stroke-width="1"/>
<path d="M25 28 C21 38 23 47 29 50 C33 47 37 45 40 41 L36 30 Z" stroke-width="1"/>
<path d="M78 40 C80 47 84 50 88 47 L86 40 Z" stroke-width="1"/>
<path d="M89 4 L87.5 -5 L93.5 1.5 Z" stroke-width="1.4"/>
<path d="M70 21 L72 14 L75 18 L78 10 L80 15 L84 5 L87 7 L78 22 Z" stroke-width="1"/>
<path d="M83 42 L96 54 L111 51" fill="none" stroke-width="4.6"/>
<path d="M76 44 L84 58 L78 71" fill="none" stroke-width="4.6"/>
<path d="M33 37 L20 54 L4 61" fill="none" stroke-width="5.6"/>
<path d="M43 43 L54 58 L49 75" fill="none" stroke-width="5"/>
</g>'''
