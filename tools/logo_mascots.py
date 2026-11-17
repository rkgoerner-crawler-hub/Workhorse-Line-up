# Mascot heads in the same sports-logo style as the horse: dark outline, three tones, fierce look.
# Each returns the drawing for a 128x128 box, without the background tile.
INK = '#160B04'
STEAM = '<g fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" opacity=".9"><path d="M{a} 106 Q{b} 104 {c} 108"/><path d="M{d} 113 Q{e} 113 {f} 118"/></g>'

def horse_art():
    import re, sys
    sys.path.insert(0, '/home/claude/brand')
    from mascot import mascot
    s = mascot('#000', size=128)
    s = s[s.index('>') + 1:s.rindex('</svg>')]
    s = s.replace('<rect width="128" height="128" rx="28" fill="#000"/>', '')
    return re.sub(r'<!--.*?-->', '', s)

def bull_art(base='#3E2516', shadow='#26160C', light='#5C3B25', horn='#EFE6D2', hornsh='#C9B998', muzzle='#7A5640', ring='#E9B44C'):
    return f'''
<g stroke="{INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round">
  <path d="M42 42 C30 44 18 38 14 24 C13 18 15 12 18 9 C20 18 26 26 40 30 Z" fill="{horn}"/>
  <path d="M86 42 C98 44 110 38 114 24 C115 18 113 12 110 9 C108 18 102 26 88 30 Z" fill="{horn}"/>
  <path d="M38 50 L16 52 L22 60 L38 60 Z" fill="{base}"/>
  <path d="M90 50 L112 52 L106 60 L90 60 Z" fill="{base}"/>
  <path d="M64 26 L44 31 L36 44 L36 60 L42 76 L44 92 Q46 112 64 115 Q82 112 84 92 L86 76 L92 60 L92 44 L84 31 Z" fill="{base}"/>
</g>
<path d="M20 26 C24 30 30 32 38 33 L40 30 C28 27 22 20 19 12 C18 16 18 22 20 26 Z" fill="{hornsh}"/>
<path d="M108 26 C104 30 98 32 90 33 L88 30 C100 27 106 20 109 12 C110 16 110 22 108 26 Z" fill="{hornsh}"/>
<path d="M37 45 L37 60 L43 76 L48 76 L43 58 L42 46 Z" fill="{shadow}"/>
<path d="M91 45 L91 60 L85 76 L80 76 L85 58 L86 46 Z" fill="{light}"/>
<path d="M46 88 Q46 112 64 113 Q82 112 82 88 Q74 80 64 80 Q54 80 46 88 Z" fill="{muzzle}" stroke="{INK}" stroke-width="2.2"/>
<path d="M52 33 Q56 26 62 31 Q64 25 68 31 Q73 26 76 33 Q70 36 64 40 Q58 36 52 33 Z" fill="{shadow}" stroke="{INK}" stroke-width="2"/>
<path d="M39 47 L58 54 L55 59 L42 55 Z" fill="{INK}"/><path d="M89 47 L70 54 L73 59 L86 55 Z" fill="{INK}"/>
<path d="M44 52 L52 55 L50 57 L45 55.6 Z" fill="#E8463A"/><path d="M84 52 L76 55 L78 57 L83 55.6 Z" fill="#E8463A"/>
<path d="M36 43 L59 50 L58 53 L37 47 Z" fill="{INK}"/><path d="M92 43 L69 50 L70 53 L91 47 Z" fill="{INK}"/>
<path d="M52 98 Q47 91 53 87 Q58 90 57 97 Z" fill="{INK}"/><path d="M76 98 Q81 91 75 87 Q70 90 71 97 Z" fill="{INK}"/>
<path d="M58 104 Q58 113 64 113 Q70 113 70 104" fill="none" stroke="{ring}" stroke-width="3.2" stroke-linecap="round"/>
<g fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" opacity=".9"><path d="M42 96 Q35 94 31 98"/><path d="M41 104 Q32 104 26 109"/><path d="M86 96 Q93 94 97 98"/><path d="M87 104 Q96 104 102 109"/></g>'''

def wolf_art(base='#7C8693', shadow='#535C68', light='#B5BDC8', white='#ECEFF3', eye='#F2C230'):
    return f'''
<g stroke="{INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round">
  <path d="M64 30 L48 33 L40 20 L30 6 L33 30 L27 43 L16 50 L28 55 L24 65 L37 67 L46 84 L55 102 Q64 110 73 102 L82 84 L91 67 L104 65 L100 55 L112 50 L101 43 L95 30 L98 6 L88 20 L80 33 Z" fill="{base}"/>
</g>
<path d="M36 28 L33 12 L42 24 Z" fill="{shadow}"/><path d="M92 28 L95 12 L86 24 Z" fill="{shadow}"/>
<path d="M29 44 L19 50 L30 54 L27 63 L38 65 L44 76 L48 72 L40 58 L36 46 Z" fill="{shadow}"/>
<path d="M99 44 L109 50 L98 54 L101 63 L90 65 L84 76 L80 72 L88 58 L92 46 Z" fill="{light}"/>
<path d="M64 46 Q74 54 77 66 L74 86 Q70 100 64 103 Q58 100 54 86 L51 66 Q54 54 64 46 Z" fill="{white}" stroke="{INK}" stroke-width="2"/>
<path d="M57 81 Q64 76 71 81 Q70 88 64 90 Q58 88 57 81 Z" fill="{INK}"/>
<path d="M54 94 Q64 99 74 94" fill="none" stroke="{INK}" stroke-width="2.2" stroke-linecap="round"/>
<path d="M57 95 L59 101 L61 96 Z M71 95 L69 101 L67 96 Z" fill="#FFFFFF" stroke="{INK}" stroke-width="1.2" stroke-linejoin="round"/>
<path d="M38 50 L56 56 L52 61 L41 58 Z" fill="{INK}"/><path d="M90 50 L72 56 L76 61 L87 58 Z" fill="{INK}"/>
<path d="M42.5 55 L51 57.6 L49.4 59.3 L43.6 57.8 Z" fill="{eye}"/><path d="M85.5 55 L77 57.6 L78.6 59.3 L84.4 57.8 Z" fill="{eye}"/>
<path d="M36 46 L57 52 L56 55 L37 50 Z" fill="{INK}"/><path d="M92 46 L71 52 L72 55 L91 50 Z" fill="{INK}"/>
<path d="M58 36 L64 44 L70 36" fill="none" stroke="{shadow}" stroke-width="2" stroke-linecap="round"/>'''

def bear_art(base='#5B3A21', shadow='#3B2413', light='#7D5634', muzzle='#B38B62', eye='#F2C230'):
    return f'''
<g stroke="{INK}" stroke-width="2.6" stroke-linejoin="round">
  <circle cx="34" cy="30" r="13" fill="{base}"/><circle cx="94" cy="30" r="13" fill="{base}"/>
  <path d="M64 24 Q38 24 30 42 Q22 60 30 80 Q40 106 64 110 Q88 106 98 80 Q106 60 98 42 Q90 24 64 24 Z" fill="{base}"/>
</g>
<circle cx="34" cy="31" r="6.5" fill="{shadow}"/><circle cx="94" cy="31" r="6.5" fill="{shadow}"/>
<path d="M31 46 Q25 62 32 79 Q38 94 46 99 Q38 82 38 64 Q38 52 31 46 Z" fill="{shadow}"/>
<path d="M97 46 Q103 62 96 79 Q90 94 82 99 Q90 82 90 64 Q90 52 97 46 Z" fill="{light}"/>
<path d="M46 80 Q46 66 64 64 Q82 66 82 80 Q82 100 64 104 Q46 100 46 80 Z" fill="{muzzle}" stroke="{INK}" stroke-width="2.2"/>
<path d="M55 72 Q64 66 73 72 Q72 80 64 82 Q56 80 55 72 Z" fill="{INK}"/>
<path d="M64 82 V88 M52 92 Q64 98 76 92" fill="none" stroke="{INK}" stroke-width="2.2" stroke-linecap="round"/>
<path d="M55 93 L57 99 L59 94.5 Z M73 93 L71 99 L69 94.5 Z" fill="#FFFFFF" stroke="{INK}" stroke-width="1.2" stroke-linejoin="round"/>
<path d="M38 48 L56 54 L52 59 L41 56 Z" fill="{INK}"/><path d="M90 48 L72 54 L76 59 L87 56 Z" fill="{INK}"/>
<path d="M42.5 53 L51 55.6 L49.4 57.3 L43.6 55.8 Z" fill="{eye}"/><path d="M85.5 53 L77 55.6 L78.6 57.3 L84.4 55.8 Z" fill="{eye}"/>
<path d="M36 44 L57 50 L56 53 L37 48 Z" fill="{INK}"/><path d="M92 44 L71 50 L72 53 L91 48 Z" fill="{INK}"/>'''

def hawk_art(base='#6B4423', shadow='#47290F', head='#C98B3C', beak='#F2B52B', beaksh='#C9871A', eye='#F2C230'):
    # Side profile facing right.
    return f'''
<g stroke="{INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round">
  <path d="M30 120 L22 96 L12 92 L24 86 L16 72 L30 72 L26 56 L40 62 L34 48 L45 47 L40 36 L52 37 L50 28 Q60 22 74 22 Q94 24 100 40 L112 48 Q120 56 116 70 L108 64 L102 70 Q96 82 84 88 L84 120 Z" fill="{base}"/>
</g>
<path d="M46 42 Q54 26 74 26 Q92 28 97 42 L94 56 Q84 66 70 66 Q54 64 46 52 Z" fill="{head}"/>
<path d="M30 116 L26 98 L38 92 L34 80 L46 82 L48 70 L60 76 L84 88 L84 116 Z" fill="{shadow}" opacity=".55"/>
<path d="M96 40 L112 48 Q120 56 116 70 L108 64 L102 70 Q99 60 92 56 Z" fill="{beak}" stroke="{INK}" stroke-width="2.4" stroke-linejoin="round"/>
<path d="M108 64 L102 70 Q100 64 96 61 Q104 61 108 64 Z" fill="{beaksh}"/>
<path d="M104 50 Q106 52 105 54" fill="none" stroke="{INK}" stroke-width="1.8" stroke-linecap="round"/>
<path d="M72 40 L92 42 L88 50 L76 50 Z" fill="{INK}"/>
<path d="M78 44 L88 45 L86 48 L79 47.5 Z" fill="{eye}"/><circle cx="84" cy="46.2" r="1.3" fill="{INK}"/>
<path d="M66 36 L96 36 L94 40 L70 40 Z" fill="{INK}"/>
<path d="M54 70 L62 78 M60 64 L70 74 M48 58 L54 64" stroke="{INK}" stroke-width="1.8" stroke-linecap="round" opacity=".7"/>'''

def shark_art(top='#5E7E96', shadow='#3F5A6E', belly='#EEF2F5', gum='#C2394A'):
    # Side profile facing right, mouth open.
    return f'''
<g stroke="{INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round">
  <path d="M8 74 L22 60 L18 40 L36 54 Q50 40 74 36 L84 14 L92 38 Q108 42 118 58 L120 64 L96 66 L120 74 Q108 92 84 96 Q58 100 36 88 L20 100 L22 82 Z" fill="{top}"/>
</g>
<path d="M36 88 Q58 100 84 96 Q108 92 120 74 L96 66 L80 72 Q58 82 32 80 Z" fill="{belly}"/>
<path d="M96 66 L120 64 L120 74 Z" fill="{gum}" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>
<path d="M99 66 L101 70 L103 66 L105 70 L107 66 L109 70 L111 65.5 L113 70 L115 65.5 L117 69 Z" fill="#FFFFFF" stroke="{INK}" stroke-width="1" stroke-linejoin="round"/>
<path d="M100 73 L102 69.6 L104 73.4 L106 69.8 L108 73.8 L110 70 L112 74 L114 70.4 L116 74 Z" fill="#FFFFFF" stroke="{INK}" stroke-width="1" stroke-linejoin="round"/>
<path d="M18 40 L36 54 L32 58 Z M84 14 L92 38 L86 38 Z" fill="{shadow}"/>
<path d="M88 48 L104 52 L100 57 L90 55 Z" fill="{INK}"/><circle cx="96" cy="53" r="1.4" fill="#FFFFFF"/>
<path d="M60 58 Q63 66 60 74 M66 57 Q69 65 66 73 M72 56 Q75 64 72 72" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>
<path d="M58 84 L70 98 L74 86 Z" fill="{top}" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round"/>'''

def football_art(ball='#8B4A22', ballsh='#5E2F12', lace='#FFFFFF', flame1='#FF6A00', flame2='#FFC21A'):
    return f'''
<path d="M8 90 C18 84 22 70 18 60 C28 66 30 56 28 46 C38 56 44 50 44 40 C50 50 56 52 62 48 L70 96 Q40 108 8 90 Z" fill="{flame1}" stroke="{INK}" stroke-width="2.4" stroke-linejoin="round"/>
<path d="M22 90 C28 84 30 76 28 70 C36 74 38 66 37 60 C44 66 48 62 50 56 L62 92 Q42 100 22 90 Z" fill="{flame2}"/>
<g transform="rotate(-32 74 66)">
  <path d="M30 66 C46 40 102 40 118 66 C102 92 46 92 30 66 Z" fill="{ball}" stroke="{INK}" stroke-width="2.8" stroke-linejoin="round"/>
  <path d="M30 66 C46 52 102 52 118 66 C102 80 46 80 30 66 Z" fill="none"/>
  <path d="M40 54 Q38 66 40 78 M108 54 Q110 66 108 78" fill="none" stroke="{lace}" stroke-width="3" stroke-linecap="round"/>
  <path d="M60 50 Q74 47 88 50" fill="none" stroke="{ballsh}" stroke-width="3" stroke-linecap="round" opacity=".7"/>
  <path d="M62 66 H86" stroke="{lace}" stroke-width="3.2" stroke-linecap="round"/>
  <path d="M66 61 V71 M71 61 V71 M76 61 V71 M81 61 V71" stroke="{lace}" stroke-width="2.6" stroke-linecap="round"/>
</g>'''

MASCOTS = [('horse', 'Horse', horse_art), ('bull', 'Bull', bull_art), ('wolf', 'Wolf', wolf_art), ('bear', 'Bear', bear_art),
           ('hawk', 'Hawk', hawk_art), ('shark', 'Shark', shark_art), ('fireball', 'Fireball', football_art)]
