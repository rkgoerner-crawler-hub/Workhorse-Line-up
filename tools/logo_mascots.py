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

def cat_art(fur='#E8892B', stripe='#B35A10', light='#F4A85A', muzzle='#FBEBD2', nose='#E86A86', lens='#121722', frame='#0B0E14'):
    # A cool cat in sunglasses, front view, with a smirk.
    return f'''
<g stroke="{INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round">
  <path d="M28 52 L22 14 L52 32 Z" fill="{fur}"/><path d="M100 52 L106 14 L76 32 Z" fill="{fur}"/>
  <path d="M64 28 Q92 28 102 46 Q112 64 104 82 Q96 104 64 108 Q32 104 24 82 Q16 64 26 46 Q36 28 64 28 Z" fill="{fur}"/>
</g>
<path d="M29 44 L26 22 L44 33 Z" fill="{nose}" opacity=".75"/><path d="M99 44 L102 22 L84 33 Z" fill="{nose}" opacity=".75"/>
<path d="M57 31 L59 41 M64 30 V42 M71 31 L69 41" fill="none" stroke="{stripe}" stroke-width="3.2" stroke-linecap="round"/>
<path d="M22 66 L32 66 M21 74 L31 72 M106 66 L96 66 M107 74 L97 72" stroke="{stripe}" stroke-width="3.2" stroke-linecap="round"/>
<path d="M98 50 Q108 66 102 82 Q96 96 84 102 Q94 84 94 68 Q94 56 98 50 Z" fill="{light}" opacity=".7"/>
<path d="M44 84 Q44 72 64 72 Q84 72 84 84 Q84 100 64 102 Q44 100 44 84 Z" fill="{muzzle}" stroke="{INK}" stroke-width="2.2"/>
<path d="M58 78 L70 78 L64 85 Z" fill="{nose}" stroke="{INK}" stroke-width="1.8" stroke-linejoin="round"/>
<path d="M64 85 V89 M64 89 Q58 95 53 91 M64 89 Q71 94 77 88" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>
<path d="M44 86 L22 84 M44 90 L24 94 M84 86 L106 84 M84 90 L104 94" stroke="#FFFFFF" stroke-width="1.6" stroke-linecap="round"/>
<!-- sunglasses -->
<path d="M26 52 L102 52 L100 58 L96 58 Q94 72 80 71 Q68 70 66 59 L62 59 Q60 70 48 71 Q34 72 32 58 L28 58 Z" fill="{frame}" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round"/>
<path d="M35 57 Q36 68 48 68 Q58 67 60 57 Z" fill="{lens}"/><path d="M68 57 Q70 67 80 68 Q92 68 93 57 Z" fill="{lens}"/>
<path d="M39 58 L47 58 L40 65 Z M72 58 L80 58 L73 65 Z" fill="#FFFFFF" opacity=".55"/>'''

def dragon_art(scale='#3E8E41', dark='#22602A', light='#6CB86A', plate='#E8C547', horn='#EFE6D2', eye='#FF4D2E', fire='#FF8A1F'):
    # Front view: swept-back horns, side frills, smoking nostrils, glowing eyes.
    return f'''
<g stroke="{INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round">
  <path d="M42 34 C34 22 24 14 10 12 C18 20 24 30 30 44 Z" fill="{horn}"/>
  <path d="M86 34 C94 22 104 14 118 12 C110 20 104 30 98 44 Z" fill="{horn}"/>
  <path d="M32 50 L8 44 L18 56 L6 64 L22 68 L14 80 L34 76 Z" fill="{dark}"/>
  <path d="M96 50 L120 44 L110 56 L122 64 L106 68 L114 80 L94 76 Z" fill="{dark}"/>
  <path d="M64 24 L46 28 L34 42 L32 62 L40 80 L44 96 Q48 116 64 118 Q80 116 84 96 L88 80 L96 62 L94 42 L82 28 Z" fill="{scale}"/>
</g>
<path d="M33 45 L33 62 L40 79 L46 78 L40 60 L40 46 Z" fill="{dark}"/>
<path d="M95 45 L95 62 L88 79 L82 78 L88 60 L88 46 Z" fill="{light}"/>
<path d="M56 30 L64 22 L72 30 L68 34 L64 30 L60 34 Z" fill="{dark}" stroke="{INK}" stroke-width="1.8" stroke-linejoin="round"/>
<path d="M52 40 Q64 36 76 40 M54 47 Q64 43 74 47" fill="none" stroke="{dark}" stroke-width="2" stroke-linecap="round"/>
<path d="M50 82 L78 82 L80 98 Q76 114 64 115 Q52 114 48 98 Z" fill="{plate}" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round"/>
<path d="M52 92 H76 M53 102 H75" stroke="{INK}" stroke-width="1.6" opacity=".45"/>
<path d="M53 89 Q50 84 55 82 Q58 85 57 89 Z M75 89 Q78 84 73 82 Q70 85 71 89 Z" fill="{INK}"/>
<path d="M36 54 L57 60 L53 66 L40 63 Z" fill="{INK}"/><path d="M92 54 L71 60 L75 66 L88 63 Z" fill="{INK}"/>
<path d="M41 60 L51 62.6 L49 64.8 L42.4 63.4 Z" fill="{eye}"/><path d="M87 60 L77 62.6 L79 64.8 L85.6 63.4 Z" fill="{eye}"/>
<path d="M34 49 L58 56 L57 59 L35 53 Z" fill="{INK}"/><path d="M94 49 L70 56 L71 59 L93 53 Z" fill="{INK}"/>
<path d="M56 108 L58 113 L60 109 Z M72 108 L70 113 L68 109 Z" fill="#FFFFFF" stroke="{INK}" stroke-width="1" stroke-linejoin="round"/>
<g fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" opacity=".8"><path d="M47 90 Q38 92 34 100"/><path d="M45 97 Q36 102 34 110"/><path d="M81 90 Q90 92 94 100"/><path d="M83 97 Q92 102 94 110"/></g>'''

def lion_art(mane='#8E4513', mane2='#B85F1C', face='#DFA457', shade='#B8792F', muzzle='#F5DCAE', eye='#F2C230'):
    spikes = 'M64 4 L74 16 L88 8 L92 22 L108 18 L106 34 L122 36 L114 50 L126 60 L114 70 L124 84 L108 88 L112 104 L96 102 L94 118 L80 110 L72 124 L64 112 L56 124 L48 110 L34 118 L32 102 L16 104 L20 88 L4 84 L14 70 L2 60 L14 50 L6 36 L22 34 L20 18 L36 22 L40 8 L54 16 Z'
    return f'''
<path d="{spikes}" fill="{mane}" stroke="{INK}" stroke-width="2.6" stroke-linejoin="round"/>
<path d="M64 16 L72 26 L84 20 L88 32 L100 30 L100 42 L112 46 L106 56 L116 64 L106 72 L112 84 L100 86 L102 98 L90 98 L88 108 L76 102 L64 110 L52 102 L40 108 L38 98 L26 98 L28 86 L16 84 L22 72 L12 64 L22 56 L16 46 L28 42 L28 30 L40 32 L44 20 L56 26 Z" fill="{mane2}"/>
<path d="M64 32 Q86 32 92 50 Q98 68 90 84 Q82 100 64 104 Q46 100 38 84 Q30 68 36 50 Q42 32 64 32 Z" fill="{face}" stroke="{INK}" stroke-width="2.6" stroke-linejoin="round"/>
<path d="M37 52 Q32 68 39 84 Q45 95 52 100 Q44 84 44 68 Q44 58 37 52 Z" fill="{shade}"/>
<path d="M60 52 Q64 62 62 72 M68 52 Q64 62 66 72" fill="none" stroke="{shade}" stroke-width="2" stroke-linecap="round" opacity=".8"/>
<path d="M46 86 Q46 74 64 74 Q82 74 82 86 Q82 100 64 102 Q46 100 46 86 Z" fill="{muzzle}" stroke="{INK}" stroke-width="2.2"/>
<path d="M56 72 Q64 66 72 72 L68 80 Q64 82 60 80 Z" fill="{INK}"/>
<path d="M64 82 V87 M64 87 Q57 94 51 90 M64 87 Q71 94 77 90" fill="none" stroke="{INK}" stroke-width="2.1" stroke-linecap="round"/>
<path d="M56 92 L58 97 L60 93 Z M72 92 L70 97 L68 93 Z" fill="#FFFFFF" stroke="{INK}" stroke-width="1.1" stroke-linejoin="round"/>
<path d="M40 54 L57 59 L53 64 L43 61.5 Z" fill="{INK}"/><path d="M88 54 L71 59 L75 64 L85 61.5 Z" fill="{INK}"/>
<path d="M44 58.6 L52 60.8 L50.4 62.6 L45 61.2 Z" fill="{eye}"/><path d="M84 58.6 L76 60.8 L77.6 62.6 L83 61.2 Z" fill="{eye}"/>
<path d="M38 50 L58 55.5 L57 58.5 L39 54 Z" fill="{INK}"/><path d="M90 50 L70 55.5 L71 58.5 L89 54 Z" fill="{INK}"/>'''

def gorilla_art(fur='#2C2C35', fur2='#45454F', face='#6A6575', faceL='#857F90', eye='#F2C230'):
    return f'''
<g stroke="{INK}" stroke-width="2.6" stroke-linejoin="round">
  <path d="M64 12 Q92 12 104 32 Q116 52 110 78 Q104 108 64 116 Q24 108 18 78 Q12 52 24 32 Q36 12 64 12 Z" fill="{fur}"/>
  <circle cx="18" cy="66" r="9" fill="{face}"/><circle cx="110" cy="66" r="9" fill="{face}"/>
</g>
<path d="M50 18 Q64 10 78 18 Q70 20 64 26 Q58 20 50 18 Z" fill="{fur2}"/>
<path d="M64 38 Q90 38 96 56 Q100 70 92 82 Q96 96 86 106 Q76 114 64 114 Q52 114 42 106 Q32 96 36 82 Q28 70 32 56 Q38 38 64 38 Z" fill="{face}" stroke="{INK}" stroke-width="2.4" stroke-linejoin="round"/>
<path d="M44 84 Q40 98 50 106 Q58 110 64 110 Q70 110 78 106 Q88 98 84 84 Q74 78 64 78 Q54 78 44 84 Z" fill="{faceL}"/>
<path d="M30 52 Q46 42 62 52 L60 58 Q46 52 32 60 Z" fill="{fur}" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>
<path d="M98 52 Q82 42 66 52 L68 58 Q82 52 96 60 Z" fill="{fur}" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>
<path d="M40 60 L56 60 L53 66 L43 65 Z" fill="{INK}"/><path d="M88 60 L72 60 L75 66 L85 65 Z" fill="{INK}"/>
<path d="M44 61.5 L52 61.5 L50.6 64 L45.2 63.6 Z" fill="{eye}"/><path d="M84 61.5 L76 61.5 L77.4 64 L82.8 63.6 Z" fill="{eye}"/>
<path d="M56 66 Q64 64 72 66 L74 78 Q64 82 54 78 Z" fill="{faceL}" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>
<path d="M57 77 Q55 72 59 71 Q62 73 61 77 Z M71 77 Q73 72 69 71 Q66 73 67 77 Z" fill="{INK}"/>
<path d="M50 94 Q64 88 78 94 Q76 102 64 104 Q52 102 50 94 Z" fill="{INK}"/>
<path d="M54 94 L57 99 L59 94.5 Z M74 94 L71 99 L69 94.5 Z" fill="#FFFFFF"/>'''

def panda_art(white='#F4F4F2', black='#16161B', shade='#D8D8D4', eye='#FF5A3C'):
    return f'''
<g stroke="{INK}" stroke-width="2.6" stroke-linejoin="round">
  <circle cx="32" cy="30" r="14" fill="{black}"/><circle cx="96" cy="30" r="14" fill="{black}"/>
  <path d="M64 22 Q96 22 106 46 Q114 66 104 86 Q92 110 64 112 Q36 110 24 86 Q14 66 22 46 Q32 22 64 22 Z" fill="{white}"/>
</g>
<path d="M24 50 Q18 68 26 86 Q34 102 46 108 Q34 88 34 68 Q34 56 24 50 Z" fill="{shade}"/>
<path d="M34 52 Q42 42 56 50 Q62 58 58 70 Q52 78 42 74 Q32 68 34 52 Z" fill="{black}" transform="rotate(-8 46 60)"/>
<path d="M94 52 Q86 42 72 50 Q66 58 70 70 Q76 78 86 74 Q96 68 94 52 Z" fill="{black}" transform="rotate(8 82 60)"/>
<path d="M41 57 L54 61 L51.6 64 L43.4 62 Z" fill="{eye}"/><path d="M87 57 L74 61 L76.4 64 L84.6 62 Z" fill="{eye}"/>
<path d="M38 50 L57 55 L56 58 L39 54 Z" fill="#FFFFFF" opacity=".0"/>
<path d="M46 86 Q46 76 64 76 Q82 76 82 86 Q82 100 64 102 Q46 100 46 86 Z" fill="#FFFFFF" stroke="{INK}" stroke-width="2"/>
<path d="M56 78 Q64 73 72 78 Q70 85 64 86 Q58 85 56 78 Z" fill="{black}"/>
<path d="M64 86 V90 M54 94 Q64 99 74 94" fill="none" stroke="{INK}" stroke-width="2.1" stroke-linecap="round"/>
<path d="M57 94.6 L59 99 L61 95.4 Z M71 94.6 L69 99 L67 95.4 Z" fill="#FFFFFF" stroke="{INK}" stroke-width="1" stroke-linejoin="round"/>
<path d="M38 48 L56 53 L55 56.4 L39 52 Z" fill="{black}"/><path d="M90 48 L72 53 L73 56.4 L89 52 Z" fill="{black}"/>'''

MASCOTS += [('cat', 'Cool cat', cat_art), ('dragon', 'Dragon', dragon_art), ('lion', 'Lion', lion_art), ('gorilla', 'Gorilla', gorilla_art), ('panda', 'Panda', panda_art)]

def eyes(l, r, col, brow=INK):
    # Angled fierce eye pair: l/r are (x, y) centers.
    (lx, ly), (rx, ry) = l, r
    return (f'<path d="M{lx-9} {ly-5} L{lx+8} {ly} L{lx+5} {ly+5} L{lx-6} {ly+3} Z" fill="{INK}"/>'
            f'<path d="M{rx+9} {ry-5} L{rx-8} {ry} L{rx-5} {ry+5} L{rx+6} {ry+3} Z" fill="{INK}"/>'
            f'<path d="M{lx-5} {ly} L{lx+3} {ly+2.2} L{lx+1.5} {ly+4} L{lx-4} {ly+2.8} Z" fill="{col}"/>'
            f'<path d="M{rx+5} {ry} L{rx-3} {ry+2.2} L{rx-1.5} {ry+4} L{rx+4} {ry+2.8} Z" fill="{col}"/>'
            f'<path d="M{lx-11} {ly-9} L{lx+10} {ly-3} L{lx+9} {ly} L{lx-10} {ly-5} Z" fill="{brow}"/>'
            f'<path d="M{rx+11} {ry-9} L{rx-10} {ry-3} L{rx-9} {ry} L{rx+10} {ry-5} Z" fill="{brow}"/>')

def tiger_art(fur='#F08A24', light='#FFB55C', white='#FFF6EA', stripe='#1E120A', eye='#9BE15D'):
    return f'''
<g stroke="{INK}" stroke-width="2.6" stroke-linejoin="round">
  <path d="M30 40 L24 16 L48 28 Z" fill="{fur}"/><path d="M98 40 L104 16 L80 28 Z" fill="{fur}"/>
  <path d="M64 24 Q94 24 104 44 L114 56 L104 60 L112 72 L100 76 Q96 104 64 112 Q32 104 28 76 L16 72 L24 60 L14 56 L24 44 Q34 24 64 24 Z" fill="{fur}"/>
</g>
<path d="M30 36 L28 22 L42 30 Z M98 36 L100 22 L86 30 Z" fill="{white}"/>
<path d="M54 30 L57 38 M64 28 V38 M74 30 L71 38 M59 40 L61 46 M69 40 L67 46" fill="none" stroke="{stripe}" stroke-width="3" stroke-linecap="round"/>
<path d="M26 52 L40 56 M24 64 L38 64 M102 52 L88 56 M104 64 L90 64" stroke="{stripe}" stroke-width="3.4" stroke-linecap="round"/>
<path d="M36 76 Q40 96 58 104 L64 92 L70 104 Q88 96 92 76 Q80 70 64 72 Q48 70 36 76 Z" fill="{white}" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round"/>
<path d="M57 72 Q64 67 71 72 Q70 79 64 80 Q58 79 57 72 Z" fill="{INK}"/>
<path d="M64 80 V86 M64 86 Q57 92 51 88 M64 86 Q71 92 77 88" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>
<path d="M55 90 L57 97 L59.5 91 Z M73 90 L71 97 L68.5 91 Z" fill="#FFFFFF" stroke="{INK}" stroke-width="1.1" stroke-linejoin="round"/>
{eyes((47, 56), (81, 56), eye)}'''

def robot_art(metal='#9AA5B4', dark='#5D6878', light='#D3DAE3', glow='#3DE8FF', bolt='#E9B44C'):
    return f'''
<path d="M64 6 V20" stroke="{INK}" stroke-width="3"/><circle cx="64" cy="7" r="5" fill="#FF4D4D" stroke="{INK}" stroke-width="2.2"/>
<g stroke="{INK}" stroke-width="2.6" stroke-linejoin="round">
  <rect x="14" y="52" width="12" height="26" rx="4" fill="{dark}"/><rect x="102" y="52" width="12" height="26" rx="4" fill="{dark}"/>
  <path d="M30 20 H98 Q106 20 106 28 V96 Q106 112 90 114 H38 Q22 112 22 96 V28 Q22 20 30 20 Z" fill="{metal}"/>
</g>
<path d="M26 26 Q26 22 32 22 H96 Q102 22 102 26 V34 H26 Z" fill="{light}" opacity=".7"/>
<path d="M23 64 V96 Q23 110 38 112 H44 Q30 104 30 90 V64 Z" fill="{dark}" opacity=".55"/>
<rect x="30" y="44" width="68" height="26" rx="10" fill="#0B1220" stroke="{INK}" stroke-width="2.4"/>
<path d="M38 52 L58 58 L56 63 L40 60 Z M90 52 L70 58 L72 63 L88 60 Z" fill="{glow}"/>
<path d="M40 54 L50 57" stroke="#FFFFFF" stroke-width="1.6" stroke-linecap="round" opacity=".8"/>
<rect x="40" y="84" width="48" height="18" rx="4" fill="{dark}" stroke="{INK}" stroke-width="2.2"/>
<path d="M48 84 V102 M56 84 V102 M64 84 V102 M72 84 V102 M80 84 V102" stroke="{INK}" stroke-width="1.8"/>
<circle cx="31" cy="30" r="2.6" fill="{bolt}" stroke="{INK}" stroke-width="1.2"/><circle cx="97" cy="30" r="2.6" fill="{bolt}" stroke="{INK}" stroke-width="1.2"/>
<circle cx="31" cy="104" r="2.6" fill="{bolt}" stroke="{INK}" stroke-width="1.2"/><circle cx="97" cy="104" r="2.6" fill="{bolt}" stroke="{INK}" stroke-width="1.2"/>'''

def rhino_art(skin='#8A919C', dark='#5E6570', light='#B4BAC3', horn='#EFE6D2', eye='#F2C230'):
    return f'''
<g stroke="{INK}" stroke-width="2.6" stroke-linejoin="round">
  <path d="M32 40 L20 20 L42 30 Z" fill="{skin}"/><path d="M96 40 L108 20 L86 30 Z" fill="{skin}"/>
  <path d="M64 26 Q90 26 98 44 Q104 60 98 74 L96 92 Q92 114 64 116 Q36 114 32 92 L30 74 Q24 60 30 44 Q38 26 64 26 Z" fill="{skin}"/>
  <path d="M52 80 Q54 46 64 18 Q74 46 76 80 Z" fill="{horn}"/>
  <path d="M56 56 Q58 44 64 36 Q70 44 72 56 Z" fill="{horn}"/>
</g>
<path d="M31 46 Q26 60 31 74 L33 92 Q36 108 48 113 Q40 98 40 84 L38 60 Z" fill="{dark}"/>
<path d="M40 92 Q44 110 64 112 Q84 110 88 92 Q78 86 64 86 Q50 86 40 92 Z" fill="{light}" stroke="{INK}" stroke-width="2.2"/>
<path d="M50 100 Q46 94 51 91 Q55 94 54 100 Z M78 100 Q82 94 77 91 Q73 94 74 100 Z" fill="{INK}"/>
<path d="M54 107 Q64 110 74 107" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>
<path d="M30 54 Q36 60 32 68 M98 54 Q92 60 96 68" fill="none" stroke="{dark}" stroke-width="2" stroke-linecap="round"/>
{eyes((40, 62), (88, 62), eye)}'''

def owl_art(feather='#7A4E2C', dark='#4E2F17', light='#A97A4E', face='#E9D3AE', beak='#F2B52B', eye='#FFB21A'):
    return f'''
<g stroke="{INK}" stroke-width="2.6" stroke-linejoin="round">
  <path d="M26 46 L16 10 L46 30 Z" fill="{feather}"/><path d="M102 46 L112 10 L82 30 Z" fill="{feather}"/>
  <path d="M64 24 Q100 24 108 54 Q114 84 94 104 Q80 118 64 118 Q48 118 34 104 Q14 84 20 54 Q28 24 64 24 Z" fill="{feather}"/>
</g>
<path d="M26 40 L22 18 L40 32 Z M102 40 L106 18 L88 32 Z" fill="{dark}"/>
<path d="M44 96 L50 104 M54 100 L60 108 M68 100 L74 108 M78 96 L84 104 M58 90 L64 98 M70 90 L74 96" stroke="{dark}" stroke-width="2" stroke-linecap="round"/>
<circle cx="45" cy="62" r="19" fill="{face}" stroke="{INK}" stroke-width="2.4"/><circle cx="83" cy="62" r="19" fill="{face}" stroke="{INK}" stroke-width="2.4"/>
<circle cx="47" cy="64" r="10" fill="{eye}" stroke="{INK}" stroke-width="2"/><circle cx="81" cy="64" r="10" fill="{eye}" stroke="{INK}" stroke-width="2"/>
<circle cx="48" cy="65" r="5" fill="{INK}"/><circle cx="80" cy="65" r="5" fill="{INK}"/>
<circle cx="50" cy="62.5" r="1.6" fill="#FFFFFF"/><circle cx="82" cy="62.5" r="1.6" fill="#FFFFFF"/>
<path d="M24 46 L62 58 L60 52 L28 40 Z M104 46 L66 58 L68 52 L100 40 Z" fill="{dark}" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>
<path d="M58 70 L70 70 L64 88 Z" fill="{beak}" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round"/>'''

def gator_art(skin='#4E8B3A', dark='#2F5E22', belly='#D9D29A', gum='#C2394A', eye='#F2C230'):
    # Side profile facing right, jaws open.
    return f'''
<g stroke="{INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round">
  <path d="M6 70 Q8 44 34 38 L50 30 Q60 26 66 34 L120 46 Q124 50 120 56 L66 62 L34 72 Z" fill="{skin}"/>
  <path d="M34 72 L66 66 L118 74 Q122 80 116 84 L60 90 Q30 96 10 88 Q4 80 6 70 Z" fill="{belly}"/>
</g>
<path d="M66 62 L120 56 L118 74 L66 66 Z" fill="{gum}" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>
<path d="M70 61 L72 66 L75 60.6 L77 65.6 L80 60.2 L82 65.2 L85 59.8 L87 64.8 L90 59.4 L92 64.4 L95 59 L97 64 L100 58.6 L102 63.6 L105 58.2 L107 63.2 L110 57.8 L112 62.6 L116 57 Z" fill="#FFFFFF" stroke="{INK}" stroke-width=".9" stroke-linejoin="round"/>
<path d="M70 66.6 L72 62.4 L75 67 L77 62.8 L80 67.4 L82 63.2 L85 67.8 L87 63.6 L90 68.2 L92 64 L95 68.6 L97 64.4 L100 69 L102 64.8 L105 69.4 L107 65.2 L110 69.8 L112 65.6 L116 70.4 Z" fill="#FFFFFF" stroke="{INK}" stroke-width=".9" stroke-linejoin="round"/>
<path d="M18 52 L24 46 M28 46 L34 42 M40 40 L44 36 M14 64 L20 60 M26 58 L32 54" stroke="{dark}" stroke-width="3" stroke-linecap="round"/>
<path d="M50 30 Q58 22 66 30 L64 38 L50 36 Z" fill="{dark}" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round"/>
<path d="M52 33 L64 33 L61 37 L54 36.4 Z" fill="{eye}"/><path d="M57 33 V37" stroke="{INK}" stroke-width="1.6"/>
<path d="M48 29 L66 31 L66 28 L50 26 Z" fill="{INK}"/>
<circle cx="114" cy="48" r="1.8" fill="{INK}"/>
<path d="M30 84 Q50 86 70 82 M24 78 Q44 80 62 76" fill="none" stroke="#B5AD74" stroke-width="1.6" stroke-linecap="round"/>'''

def bulldog_art(fur='#C9A27A', dark='#8E6A45', light='#E6CDAE', muzzle='#F1E2CC', collar='#1A1A1F', spike='#D8DEE6', eye='#3A2414'):
    return f'''
<g stroke="{INK}" stroke-width="2.6" stroke-linejoin="round">
  <path d="M28 40 Q14 36 12 50 Q20 52 30 58 Z" fill="{dark}"/><path d="M100 40 Q114 36 116 50 Q108 52 98 58 Z" fill="{dark}"/>
  <path d="M64 24 Q94 24 102 44 Q110 64 106 84 Q102 104 64 108 Q26 104 22 84 Q18 64 26 44 Q34 24 64 24 Z" fill="{fur}"/>
  <path d="M18 104 Q64 126 110 104 L110 116 Q64 136 18 116 Z" fill="{collar}"/>
</g>
<path d="M30 110 L34 102 L38 112 Z M50 116 L54 107 L58 117 Z M70 117 L74 107 L78 116 Z M90 112 L94 102 L98 110 Z" fill="{spike}" stroke="{INK}" stroke-width="1.4" stroke-linejoin="round"/>
<path d="M50 34 Q64 40 78 34 M48 42 Q64 48 80 42" fill="none" stroke="{dark}" stroke-width="2.4" stroke-linecap="round"/>
<path d="M24 60 Q20 80 28 96 Q36 104 44 104 Q34 88 34 72 Z" fill="{dark}" opacity=".6"/>
<path d="M34 78 Q34 64 52 66 Q64 70 76 66 Q94 64 94 78 Q94 100 64 102 Q34 100 34 78 Z" fill="{muzzle}" stroke="{INK}" stroke-width="2.2"/>
<path d="M54 66 Q64 60 74 66 Q72 74 64 75 Q56 74 54 66 Z" fill="{INK}"/>
<path d="M64 75 V80 M44 82 Q64 74 84 82 Q82 96 64 97 Q46 96 44 82 Z" fill="{INK}" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>
<path d="M48 84 L51 78 L54 84 Z M74 84 L77 78 L80 84 Z" fill="#FFFFFF"/>
<path d="M34 80 Q30 92 40 98 M94 80 Q98 92 88 98" fill="none" stroke="{dark}" stroke-width="2" stroke-linecap="round"/>
{eyes((44, 54), (84, 54), eye)}'''

def skull_art(bone='#F1EDE4', shade='#C9C1B0', glow='#FF4D2E', dark='#14100C'):
    return f'''
<g stroke="{INK}" stroke-width="2.6" stroke-linejoin="round">
  <path d="M64 12 Q100 12 108 44 Q112 64 100 76 L98 92 Q96 100 88 100 L86 112 H42 L40 100 Q32 100 30 92 L28 76 Q16 64 20 44 Q28 12 64 12 Z" fill="{bone}"/>
</g>
<path d="M21 46 Q20 64 30 76 L32 92 Q34 98 40 99 Q36 84 36 70 Q30 58 30 44 Q30 30 40 22 Q24 28 21 46 Z" fill="{shade}"/>
<path d="M30 54 Q32 40 48 42 Q60 46 58 60 Q56 74 44 74 Q32 72 30 54 Z" fill="{dark}" stroke="{INK}" stroke-width="2"/>
<path d="M98 54 Q96 40 80 42 Q68 46 70 60 Q72 74 84 74 Q96 72 98 54 Z" fill="{dark}" stroke="{INK}" stroke-width="2"/>
<path d="M38 54 L52 58 L50 63 L40 61 Z M90 54 L76 58 L78 63 L88 61 Z" fill="{glow}"/>
<path d="M64 74 L58 88 L70 88 Z" fill="{dark}"/>
<path d="M44 100 V112 M54 100 V112 M64 100 V112 M74 100 V112 M84 100 V112" stroke="{INK}" stroke-width="2.2"/>
<path d="M42 100 H86" stroke="{INK}" stroke-width="2.2"/>
<path d="M78 20 L72 30 L80 34" fill="none" stroke="{shade}" stroke-width="2" stroke-linecap="round"/>'''

def unicorn_art(coat='#F5F2FB', shade='#D6CFE6', mane1='#8B5CF6', mane2='#EC4899', mane3='#22D3EE', horn='#F2C14E', eye='#6D28D9'):
    # Side profile facing right, like a charging horse with a gold horn.
    return f'''
<g stroke="{INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round">
  <path d="M30 120 Q26 84 40 60 Q50 40 66 30 L74 22 L82 30 Q100 38 112 58 Q120 70 116 80 Q110 86 100 82 L88 76 Q80 74 76 82 L70 120 Z" fill="{coat}"/>
  <path d="M74 24 L96 2 L84 32 Z" fill="{horn}"/>
</g>
<path d="M78 22 L90 12 M80 27 L92 15" stroke="#C99A2E" stroke-width="2" stroke-linecap="round"/>
<path d="M66 30 Q50 32 38 46 Q26 62 22 84 Q16 104 18 120 L30 120 Q30 92 40 72 Q50 52 70 40 Z" fill="{mane1}" stroke="{INK}" stroke-width="2.4" stroke-linejoin="round"/>
<path d="M60 36 Q44 46 36 64 Q30 80 28 100 L34 100 Q36 82 44 66 Q52 52 66 42 Z" fill="{mane2}"/>
<path d="M54 44 Q44 56 40 72 Q36 86 36 98 L40 98 Q42 84 46 72 Q50 60 60 50 Z" fill="{mane3}"/>
<path d="M68 26 L60 14 L74 22 Z" fill="{coat}" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round"/>
<path d="M100 82 Q110 86 116 80 Q118 72 112 66 Q104 74 100 82 Z" fill="{shade}"/>
<circle cx="111" cy="72" r="2" fill="{INK}"/>
<path d="M82 46 L98 50 L95 55 L85 53 Z" fill="{INK}"/><path d="M86 49 L94 51 L92.6 53 L87 52 Z" fill="{eye}"/>
<path d="M80 41 L100 46 L99 49 L81 45 Z" fill="{INK}"/>
<path d="M104 82 Q106 88 100 90" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>'''

MASCOTS += [('tiger', 'Tiger', tiger_art), ('robot', 'Robot', robot_art), ('rhino', 'Rhino', rhino_art), ('owl', 'Owl', owl_art),
            ('gator', 'Gator', gator_art), ('bulldog', 'Bulldog', bulldog_art), ('skull', 'Skull', skull_art), ('unicorn', 'Unicorn', unicorn_art)]
