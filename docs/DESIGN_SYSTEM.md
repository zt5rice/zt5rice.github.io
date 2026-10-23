# Portfolio Design System

Approved direction: technical editorial

Primary positioning: `Software Engineer · Data & AI Systems`

This document is the implementation authority for the portfolio visual system.
The design should remain content-first and evidence-led. Visual effects support
hierarchy; they must never hide or delay the core content.

## Mockups

- [Desktop homepage](../design/mockups/home-desktop.png)
- [Mobile homepage](../design/mockups/home-mobile.png)
- [Desktop case study](../design/mockups/case-study-desktop.png)

Regenerate the PNGs with:

```bash
python3 design/generate_mockups.py
```

The mockup generator uses local `Avenir Next` and `Menlo` stand-ins. The
implemented site must self-host `Space Grotesk` and `IBM Plex Mono` as specified
below.

## Design concept

The portfolio uses a dark technical-editorial system: near-black surfaces, bone
text, signal orange for emphasis, and monospaced labels that create a systems
vocabulary. The portrait and project evidence provide warmth and specificity.

The layout should feel engineered rather than futuristic:

- Asymmetric desktop hero with a 4:5 portrait.
- Large editorial name treatment.
- Thin grid and linework, not decorative particles.
- Orange as a directional signal, not a background wash.
- Green only for live, healthy, passed, or available states.
- Dense evidence presented with spacious type and clear grouping.

## Differentiation from the reference

The reference site proves that a concise profile README and a dark portfolio can
work. This design borrows the clarity and consistency, not the surface language.

Intentional differences:

- No full-screen portrait background.
- No green-pink status palette.
- No terminal simulation or module-selection landing state.
- No content hidden behind an “enter portfolio” screen.
- No project gallery that requires interaction before showing work.
- Orange linework and technical grid create a distinct visual identity.

## Color tokens

| Token | Value | Use |
| --- | --- | --- |
| `--bg` | `#090B0D` | Page background |
| `--surface` | `#121518` | Cards and panels |
| `--surface-raised` | `#171B1E` | Pills, inline panels |
| `--text` | `#F2EEE6` | Primary text |
| `--text-muted` | `#9EA3A6` | Body secondary text |
| `--text-dim` | `#6F767A` | Metadata and tertiary labels |
| `--accent` | `#FF6A3D` | Primary emphasis, lines, CTA |
| `--signal` | `#78F0A6` | Live, healthy, pass, focus |
| `--border` | `#2B2F32` | Default borders |
| `--border-strong` | `#3A3F43` | Hover and selected borders |

Do not introduce additional saturated colors. Project screenshots may contain
their own palettes.

### Contrast verification

| Foreground | Background | Ratio | Result |
| --- | --- | ---: | --- |
| `#F2EEE6` | `#090B0D` | 17.04:1 | AAA |
| `#9EA3A6` | `#090B0D` | 7.74:1 | AAA |
| `#FF6A3D` | `#090B0D` | 6.93:1 | AA+ |
| `#78F0A6` | `#090B0D` | 13.91:1 | AAA |
| `#090B0D` | `#FF6A3D` | 6.93:1 | AA+ |
| `#F2EEE6` | `#121518` | 15.83:1 | AAA |
| `#9EA3A6` | `#121518` | 7.19:1 | AAA |
| `#FF6A3D` | `#121518` | 6.44:1 | AA+ |

Primary and secondary text meet WCAG AA at normal sizes. Orange is not used for
long body copy.

## Typography

### Target families

- Display and body: `Space Grotesk`
- Labels, metrics, metadata, and code: `IBM Plex Mono`

Self-host both families in the final static build. Avoid a runtime dependency on
Google Fonts.

### Type scale

| Token | Desktop | Mobile | Line height | Use |
| --- | ---: | ---: | ---: | --- |
| `display-hero` | 106 px | 64 px | 0.92 | Name |
| `display-xl` | 67 px | 44 px | 0.98 | Case-study headline |
| `display-lg` | 48 px | 39 px | 1.02 | Section heading |
| `heading-md` | 30 px | 23 px | 1.12 | Hero discipline |
| `heading-sm` | 25 px | 22 px | 1.2 | Card title |
| `body-lg` | 18 px | 15 px | 1.6 | Hero paragraph |
| `body` | 15 px | 14 px | 1.55 | Standard copy |
| `body-sm` | 13 px | 13 px | 1.5 | Dense supporting copy |
| `label` | 11 px | 10 px | 1.4 | Mono labels |
| `micro` | 9 px | 9 px | 1.4 | Metadata |

Use sentence case for headings and body. Use uppercase monospaced labels for
section identifiers, categories, metrics, and control labels.

## Spacing and grid

### Spacing scale

`4, 8, 12, 16, 24, 32, 48, 64, 96, 128`

Default section spacing:

- Desktop: `96–128 px`
- Tablet: `72–96 px`
- Mobile: `56–72 px`

### Layout

- Max content width: `1280 px`
- Desktop outer margin: `96 px`
- Tablet outer margin: `48 px`
- Mobile outer margin: `24 px`
- Desktop grid: 12 columns, `24 px` gutters
- Tablet grid: 6 columns, `20 px` gutters
- Mobile grid: 4 columns, `16 px` gutters

Hero desktop ratio:

- Text: approximately 7 units
- Portrait: approximately 5 units
- Gap: `64 px`

Hero mobile:

- Text first
- Portrait after primary CTA
- Portrait continues to use the 4:5 ratio

## Shape and borders

- Cards: `12 px` radius
- Images inside cards: `8 px` radius
- Portrait frame: `12 px` image radius, `18 px` outer frame
- Buttons: `4 px` radius
- Pills: `999 px`
- Default border: `1 px solid var(--border)`
- Hover border: `var(--border-strong)`

Avoid glows around every element. Orange glow is reserved for the hero portrait
and major case-study header.

## Components

### Navigation

Desktop:

- Height `88 px`
- Sticky with `background: rgba(9, 11, 13, 0.88)`
- `backdrop-filter: blur(14px)`
- Logo and links use mono labels
- Resume CTA uses an outlined button

Mobile:

- Height `64 px`
- Logo left, menu button right
- Menu opens as a full-width sheet below the header
- Focus is trapped while the menu is open
- Escape closes it and returns focus to the menu button

### Buttons

- Minimum height `46 px`
- Horizontal padding `20–24 px`
- Mono uppercase label
- Primary: orange fill, `--bg` text
- Secondary: transparent fill, border, primary text
- Hover: background or border shift only
- Focus ring: `2 px solid var(--signal)`, `3 px` offset

### Links

- Inline links use text color and an underline offset
- Hover/focus underline color becomes orange
- External links receive an accessible label indicating a new tab when used

### Proof strip

- Desktop: four columns separated by vertical rules
- Mobile: two-column by two-row grid
- Metric value uses display-sized body type
- Supporting label uses mono micro type and sentence case

### Project card

- Surface `--surface`
- Border `--border`
- Image uses 16:9 crop at card width
- Card content uses `24 px` padding
- Category label in orange mono
- Title uses `heading-sm`
- Summary is limited to two or three lines
- Metrics use mono pills
- CTA uses `Read case study →`
- Entire card is clickable; nested links must stop propagation

### Case-study header

- Category label
- Large two-line headline
- Short deck
- Stack pills
- Three evidence stats
- Architecture and evidence follow immediately

### Media

- Static images use WebP or AVIF with explicit dimensions
- Video uses poster, click-to-play, no autoplay, no sound by default
- Do not use a video as the only source of project evidence
- Add descriptive alt text based on the visible content

## Responsive behavior

| Breakpoint | Behavior |
| --- | --- |
| `< 480 px` | Single-column cards, stacked hero, 24 px margins |
| `480–767 px` | Single-column cards, wider media, 32 px margins |
| `768–1023 px` | Two-column work grid, compact navigation, 48 px margins |
| `1024–1279 px` | Asymmetric hero, two-column cards, 64 px margins |
| `>= 1280 px` | Full layout, 96 px margins, 1280 px max content |

No horizontal overflow is allowed. Long labels must wrap or shorten before type
falls below the defined minimum.

## Motion

### Page entrance

- Hero text: `opacity 0 → 1`, `translateY 16px → 0`
- Duration: `600 ms`
- Easing: `cubic-bezier(0.22, 1, 0.36, 1)`

### Section reveal

- Triggered once by `IntersectionObserver`
- `opacity 0 → 1`, `translateY 20px → 0`
- Duration: `550 ms`
- Stagger: `70 ms` for sibling cards

### Interaction

- Button/card border and background: `160–180 ms`
- Link underline: `120 ms`
- No scaling above `1.01`
- No continuous movement except an optional status dot

### Reduced motion

When `prefers-reduced-motion: reduce`:

- Disable entrance translations
- Disable section reveals
- Disable video autoplay
- Set transition duration to `0.01 ms`
- Keep all content visible without JavaScript

## Accessibility requirements

- Semantic landmarks: header, nav, main, section, footer
- One `h1` per page
- Logical heading hierarchy
- Skip-to-content link
- Visible focus state on all interactive elements
- Keyboard-operable mobile navigation
- Reliable color contrast
- No information conveyed only by color
- Descriptive alt text and captions
- Minimum target size `44 x 44 px` on touch devices
- Respect reduced motion
- Videos have captions or an equivalent textual summary

## Portrait treatment

- Use the approved 4:5 portrait.
- Frame it inside a slightly larger panel.
- Add restrained orange rim light and grid lines outside the face.
- Do not apply beauty retouching or generative alteration.
- Do not use the portrait as a blurred full-screen background.
- On mobile, keep the portrait below the positioning and primary CTA.

## Content hierarchy

### Five-second level

- Name
- Software Engineer · Data & AI Systems
- One-sentence value proposition
- Resume and selected-work CTAs

### Thirty-second level

- Four proof metrics
- Four selected projects
- Each project’s one-line problem and strongest evidence

### Two-minute level

- Project architecture
- Engineering decisions
- Measured outcomes
- Limitations and boundaries

## Implementation notes

- Build with CSS variables matching the tokens above.
- Use CSS Grid for the page and card layouts.
- Avoid component libraries that impose a different visual system.
- Use the mockups for hierarchy and proportion, not pixel-perfect bitmap export.
- Use real text, not text baked into images.
- Use the generated project media from `public/assets/portfolio/`.
- Keep the page readable when JavaScript is unavailable.

## Approval gate

The visual direction is approved when Zhao Tang accepts:

1. Desktop hero and selected-work layout.
2. Mobile hero and project-card layout.
3. Case-study page hierarchy.
4. Charcoal, bone, orange, and restrained green palette.
5. Motion and accessibility principles.

No website scaffold or UI implementation starts until this approval is explicit.
