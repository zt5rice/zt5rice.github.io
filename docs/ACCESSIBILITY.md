# Accessibility Verification

Last reviewed: 2026-10-24

## Structural checks

- Every generated page has `lang="en"`.
- Every page has one `h1`.
- Every page has a unique title and canonical URL.
- Header, navigation, main content, sections, and footer use semantic landmarks.
- The skip link is the first keyboard-focusable element.
- All images include an `alt` attribute.
- Project-card images use an empty alt because the surrounding link has an
  accessible project-specific label.
- Video players expose native controls and do not autoplay.

## Keyboard checks

Verified browser focus order:

1. Skip to content
2. Home
3. Work
4. Experience
5. About
6. Research
7. Contact

Every tested control displays a visible `2px` focus outline with a `3px` offset.

Mobile navigation:

- Uses a native `<details>` / `<summary>` control.
- Opens with keyboard or pointer input.
- Escape closes the menu and returns focus to the summary.
- Navigation links remain available without JavaScript.

## Reduced motion

The built CSS includes `@media (prefers-reduced-motion: reduce)`.

Under reduced motion:

- Hero entrance animation is disabled.
- Project and case-study reveal transitions are disabled.
- Image hover scale is disabled.
- Smooth scrolling is disabled.
- All content remains visible regardless of JavaScript state.

The reveal controller also exits early when reduced motion is requested.

## Color and contrast

Principal combinations:

| Foreground | Background | Ratio |
| --- | --- | ---: |
| `#F2EEE6` | `#090B0D` | 17.04:1 |
| `#9EA3A6` | `#090B0D` | 7.74:1 |
| `#FF6A3D` | `#090B0D` | 6.93:1 |
| `#78F0A6` | `#090B0D` | 13.91:1 |
| `#090B0D` | `#FF6A3D` | 6.93:1 |
| `#F2EEE6` | `#121518` | 15.83:1 |
| `#9EA3A6` | `#121518` | 7.19:1 |

These meet WCAG AA at normal text sizes.

## Responsive and media checks

- 1440 px and 390 px layouts have no horizontal page overflow.
- Project media uses responsive AVIF/WebP sources.
- Animated nanotrack WebP intentionally bypasses the static responsive pipeline
  so animation is preserved.
- No `.mov` file is required by the built site.

## Remaining audit

The final Lighthouse and full cross-page automated audit runs in `ZHA-195`.
