---
version: alpha
name: Supabase
slug: supabase
source: https://supabase.com/
extractedAt: 2026-05-19
description: "Developer-first Postgres platform identity with near-black product surfaces, hairline gray borders, compact dashboard modules, monospaced labels, and a luminous Supabase green action system."

colors:
  primary: "#3ECF8E"
  accent: "#249361"
  accentHover: "#33CC87"
  accentPressed: "#15593B"
  ink: "#FAFAFA"
  body: "#B4B4B4"
  muted: "#898989"
  canvas: "#121212"
  surface: "#1F1F1F"
  surfaceAlt: "#171717"
  border: "#2E2E2E"
  borderStrong: "#454545"
  link: "#00C47C"
  success: "#3ECF8E"
  warning: "#DB8900"
  error: "#E54D2E"
  brandMist: "#EBFAF3"
  brandDeep: "#072719"
  brandPanel: "#041B10"
  dashCanvas: "#121212"
  dashSidebar: "#171717"
  codeCanvas: "#1E1E1E"
  selection: "#313131"
  focusRing: "#3ECF8E"
  on-primary: "#072719"
  on-dark: "#FAFAFA"

typography:
  display:
    fontFamily: "custom-font, Circular, Inter, Helvetica Neue, Arial, sans-serif"
    fontSize: 72px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: "0em"
  hero:
    fontFamily: "custom-font, Circular, Inter, Helvetica Neue, Arial, sans-serif"
    fontSize: 60px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: "0em"
  headline-lg:
    fontFamily: "custom-font, Circular, Inter, Helvetica Neue, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: "0em"
  title-lg:
    fontFamily: "custom-font, Circular, Inter, Helvetica Neue, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: "0em"
  title-md:
    fontFamily: "custom-font, Circular, Inter, Helvetica Neue, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: "0em"
  title-sm:
    fontFamily: "custom-font, Circular, Inter, Helvetica Neue, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: "0em"
  body:
    fontFamily: "custom-font, Circular, Inter, Helvetica Neue, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: "0em"
  label:
    fontFamily: "Source Code Pro, Office Code Pro, Menlo, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: "0.08em"
  button:
    fontFamily: "custom-font, Circular, Inter, Helvetica Neue, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: "0em"
  caption:
    fontFamily: "custom-font, Circular, Inter, Helvetica Neue, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: "0em"
  legal:
    fontFamily: "custom-font, Circular, Inter, Helvetica Neue, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: "0em"
  pricing-display:
    fontFamily: "custom-font, Circular, Inter, Helvetica Neue, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: "0em"
  code:
    fontFamily: "Source Code Pro, Office Code Pro, Menlo, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.36
    letterSpacing: "0em"

rounded:
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
  pill: 9999px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  section: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 14px
  button-primary-active:
    backgroundColor: "{colors.accentPressed}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    borderColor: "{colors.borderStrong}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 14px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 10px
  button-icon:
    backgroundColor: "{colors.surfaceAlt}"
    textColor: "{colors.body}"
    borderColor: "{colors.border}"
    rounded: "{rounded.md}"
    size: 34px
  button-pricing-pill:
    backgroundColor: "{colors.brandDeep}"
    textColor: "{colors.primary}"
    borderColor: "{colors.accentPressed}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 10px
  hero-card:
    backgroundColor: "{colors.surfaceAlt}"
    borderColor: "{colors.border}"
    rounded: "{rounded.xl}"
    padding: 24px
  feature-card:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.border}"
    rounded: "{rounded.lg}"
    padding: 24px
  dashboard-frame:
    backgroundColor: "{colors.dashCanvas}"
    borderColor: "{colors.border}"
    rounded: "{rounded.xl}"
    shadow: "none"
  code-panel:
    backgroundColor: "{colors.codeCanvas}"
    borderColor: "{colors.border}"
    rounded: "{rounded.md}"
    typography: "{typography.code}"
    padding: 16px
  pricing-card:
    backgroundColor: "{colors.surfaceAlt}"
    borderColor: "{colors.borderStrong}"
    rounded: "{rounded.lg}"
    padding: 24px
  input-default:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    borderColor: "{colors.borderStrong}"
    typography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: 8px 10px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.border}"
    height: 64px
  docs-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    borderColor: "{colors.border}"
    width: 280px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    borderColor: "{colors.border}"
    padding: 64px 0
---

**Overview**

Supabase presents itself as a serious developer platform rather than a glossy SaaS brochure. The core visual identity is a dark, product-native environment: near-black canvases, gray hairline borders, compact control surfaces, monospaced labels, code panels, and dashboard screenshots treated as first-class brand assets. The recognizable brand moment is the bright Supabase green, but the system works because that green is used with restraint against a disciplined grayscale interface.

The site has three related modes. Marketing pages use large sparse headlines, product screenshots, bordered feature tiles, and green calls to action. Pricing becomes denser and more operational, with plan cards, usage tables, calculators, and pill tags. Docs shift into a utility mode with persistent sidebars, code blocks, compact navigation, and active states that feel closer to an IDE than to a campaign page.

Key Characteristics:

- Dark-first interface language using {colors.canvas}, {colors.surface}, and {colors.border}.
- Supabase green {colors.primary} as action, success, link, glow, and brand highlight.
- Low-radius controls, usually {rounded.md} or {rounded.lg}, never bubbly.
- Thin borders and subtle surface shifts carry hierarchy more than shadows.
- Large headlines stay calm: regular weight, tight line-height, no theatrical tracking.
- Product UI modules, tables, code panels, and dashboard frames are brand signatures.
- Monospaced uppercase labels provide a technical rhythm above sections and cards.

**Colors**

Primary & Action:

{colors.primary} `#3ECF8E` is the signature Supabase green. It appears on primary actions, brand gradients, success moments, links in technical content, focus accents, and active navigation indicators.

{colors.accent} `#249361` is the deeper interactive green used for pressed, hover, and supporting action states. It lets green stay visible without making every control glow at full intensity.

{colors.accentHover} `#33CC87` is a brighter hover bridge between base action and highlight. Use it for subtle icon emphasis, badges, and progressive disclosure controls.

{colors.accentPressed} `#15593B` is the dark green active surface seen in selected pills and dark brand panels. Pair it with {colors.primary} text when the control needs to remain dark.

{colors.link} `#00C47C` is the docs and prose link color. It should feel technical and direct, closer to a terminal highlight than a consumer-blue link.

Surfaces:

{colors.canvas} `#121212` is the dominant page background in dark mode. It gives the site its product-console mood and should remain visible around major modules.

{colors.surface} `#1F1F1F` is the default card, input, and raised-control surface. It separates modules from the canvas without creating a heavy panel effect.

{colors.surfaceAlt} `#171717` is the quieter alternate surface used for large panels, hero containers, nav shells, and dashboard areas.

{colors.dashCanvas} `#121212` and {colors.dashSidebar} `#171717` capture the embedded dashboard pattern. Use them when reproducing product UI, not decorative marketing cards.

{colors.codeCanvas} `#1E1E1E` is the terminal/code background. It should be paired with {typography.code}, small line-height, and restrained syntax accents.

Neutrals & Text:

{colors.ink} `#FAFAFA` is the high-contrast foreground for headings and key values. It is crisp but slightly softened compared with pure white.

{colors.body} `#B4B4B4` is the normal paragraph and secondary label color. It keeps copy legible while preserving the dark interface tone.

{colors.muted} `#898989` is for tertiary links, metadata, footer links, captions, and inactive docs items.

{colors.border} `#2E2E2E` is the default divider and card outline. Supabase leans heavily on this token for structure.

{colors.borderStrong} `#454545` is used when a control or table edge needs firmer definition. It should still feel gray, not metallic.

Semantic:

{colors.success} uses the brand green rather than a separate success color. This reinforces the connection between "working" and Supabase action.

{colors.warning} `#DB8900` appears in cautionary product states and docs callouts. Keep it sparse so it does not compete with brand green.

{colors.error} `#E54D2E` is the destructive and invalid state color. Use it with dark red-tinted surfaces only for forms, API errors, or security warnings.

Brand-specific signatures:

{colors.brandMist} `#EBFAF3` is the lightest brand tint seen in light-mode green scales. It is useful for small inverted badges or illustrations.

{colors.brandDeep} `#072719` and {colors.brandPanel} `#041B10` are dark green support colors. They make selected pills, pricing highlights, and brand panels feel Supabase-specific without overusing bright green.

{colors.selection} `#313131` is the dark selected-row or active-item color. It keeps active UI states quiet unless a brand action is required.

**Typography**

Supabase marketing CSS defines `custom-font` and falls back through Circular, Inter, Helvetica Neue, Arial, and sans-serif. The visible voice is geometric and utilitarian: round enough to be approachable, but regular-weight and calm. Labels and code use Source Code Pro, Office Code Pro, Menlo, or monospace, giving section markers, snippets, and docs a technical cadence.

| Level | Size | Weight | Line-height | Letter-spacing |
| --- | ---: | ---: | ---: | ---: |
| {typography.display} | 72px | 400 | 1.00 | 0em |
| {typography.hero} | 60px | 400 | 1.00 | 0em |
| {typography.headline-lg} | 36px | 400 | 1.20 | 0em |
| {typography.title-lg} | 24px | 400 | 1.33 | 0em |
| {typography.title-md} | 20px | 400 | 1.40 | 0em |
| {typography.title-sm} | 16px | 500 | 1.50 | 0em |
| {typography.body} | 16px | 400 | 1.50 | 0em |
| {typography.label} | 12px | 400 | 1.33 | 0.08em |
| {typography.button} | 14px | 400 | 1.43 | 0em |
| {typography.caption} | 12px | 400 | 1.33 | 0em |
| {typography.pricing-display} | 48px | 400 | 1.00 | 0em |
| {typography.code} | 14px | 400 | 1.36 | 0em |

Principles:

- Keep display type regular-weight; hierarchy comes from scale and whitespace, not boldness.
- Avoid negative tracking. Supabase type is clean, neutral, and uncompressed.
- Use {typography.label} for technical eyebrow labels, not decorative all-caps marketing badges.
- Split prose and code clearly: body text uses custom-font, while snippets and command surfaces use {typography.code}.
- Let muted text stay muted. Supabase often uses {colors.body} and {colors.muted} instead of making every sentence bright.

**Layout**

The spacing rhythm is a Tailwind-like 4px base: {spacing.xs}, {spacing.sm}, {spacing.md}, {spacing.lg}, and {spacing.xl}. Marketing sections commonly breathe at {spacing.section} vertically, while dense docs and dashboard modules compress to 8px and 16px gaps. Page content usually sits in a centered container around 1200px to 1280px, with larger product images allowed to span wider through masked or overflow layouts.

Grids are pragmatic. Feature areas use two- or three-column cards on desktop, collapsing into single-column stacks on mobile. Pricing uses plan columns plus comparison tables, then converts to mobile card/table hybrids. Docs use a persistent left sidebar, central article column, and right table-of-contents at wide sizes.

Whitespace is generous around narrative claims but tight inside product UI. A Supabase page should feel like an elegant command center: spacious enough to read, compact enough to imply real tools, data, and engineering workflows.

**Elevation & Depth**

Supabase is mostly flat. Borders, dark surface steps, inset dividers, active rows, and screenshot framing create depth before shadows do. Cards generally use `shadow: none`, and the observed shadows are small utility shadows or code/demo presentation shadows, not glossy elevation.

Use hairline borders with {colors.border} as the default separator. Reach for {colors.borderStrong} when a pricing card, input, or dashboard frame needs definition. Shadows can appear on floating menus or docs/code previews, but should stay restrained: `0 1px 2px #0000000d`, `0 1px 3px #0000001a`, or a soft demo shadow only when a module must float over the canvas.

**Components**

Buttons:

{components.button-primary} is compact, rectangular, and green. It should be used for signup, start, create, and subscribe actions, with {colors.on-primary} text to preserve contrast against {colors.primary}.

{components.button-primary-active} is a selected or pressed brand state. Its dark green surface keeps active controls integrated into dark UI rather than turning them into bright stickers.

{components.button-secondary} is the default neutral action for docs, product pages, and pricing. It uses a dark surface and a visible border, sitting one level below the green primary button.

{components.button-ghost} supports navigation and low-priority actions. It should usually be gray until hover, where text can move toward {colors.ink}.

{components.button-icon} is a square utility control for nav, tabs, theme controls, copy buttons, and product toolbars. Use icons rather than text when the action is familiar.

{components.button-pricing-pill} marks selected billing states, plan tags, or usage categories. Its dark green fill and pill radius distinguish pricing affordances from normal rectangular dashboard controls.

Cards & Containers:

{components.hero-card} frames large product visuals or combined copy-plus-dashboard modules. It should be broad, dark, bordered, and calm, with the product screenshot doing the expressive work.

{components.feature-card} is a bordered tile for product benefits, use cases, integrations, or launch items. Keep its content compact: a small icon or label, a short title, and a restrained paragraph.

{components.dashboard-frame} is one of the most brand-specific containers. It mimics Supabase product UI with dark canvas, sidebars, tables, tabs, and code/database panels inside a rounded bordered shell.

{components.code-panel} is used for snippets, SQL, API examples, terminal commands, and docs demonstrations. It should feel like an editor surface: monospaced type, compact line-height, and minimal chrome.

Inputs & Forms:

{components.input-default} is a compact dark input with a visible border and small type. Newsletter forms, auth-like examples, calculators, and docs search all use this restrained control language.

Invalid input states should use {colors.error} only at the border, ring, or small message level. Do not flood entire forms with red.

Navigation:

{components.nav-bar} is sticky, dark, and border-led. Links are small and muted, with product and docs links becoming brighter on hover or active state.

{components.docs-sidebar} is denser than marketing navigation. It uses muted nested links, active row backgrounds, tiny labels, and border dividers to create a documentation map.

{components.footer} is a large utility index rather than a promotional block. It uses muted text, multiple columns, small headings, a newsletter input, and social icons in a restrained dark grid.

Pricing:

{components.pricing-card} holds plan tiers, feature lists, usage notes, and CTAs. It should balance sales information with product precision: clean columns, quiet borders, green highlights, and no oversized decorative pricing badges.

Pricing tables are a signature pattern. Use compact cells, strong column labels, selected green text for preferred infrastructure, and mobile-specific stacked rows instead of forcing a wide comparison table onto small screens.

Signature Components:

The dashboard product screenshot is the strongest Supabase motif. Tables, schema editors, auth panels, logs, and API/code panes should appear as real UI, not abstract illustration.

Code-led explanation blocks are another signature. Pair a short claim with a {components.code-panel} or mini editor frame whenever a feature is API-, SQL-, or CLI-driven.

Green text gradients and subtle brand glows may appear in hero headlines and launch/product moments, but only as text treatment or background accent. The normal system remains flat, dark, and bordered.

**Do's and Don'ts**

Do:

- Use {colors.canvas} as the dominant page field and layer {colors.surfaceAlt} and {colors.surface} for modules.
- Reserve {colors.primary} for real actions, active states, links, and technical highlights.
- Draw structure with {colors.border} and {colors.borderStrong} before adding shadow.
- Use {typography.label} for compact uppercase technical labels above sections.
- Keep buttons at {rounded.md} with compact padding, especially in nav and docs contexts.
- Represent product value through dashboard frames, code panels, tables, and API examples.
- Let large headlines use {typography.hero} or {typography.display} at regular weight.
- Collapse dense data into stacked cards on mobile rather than shrinking text below {typography.caption}.

Don't:

- Do not turn Supabase green into a full-page decorative wash; the brand depends on dark restraint.
- Do not use bubbly 20px+ radii for normal controls; stay near {rounded.md}, {rounded.lg}, and {rounded.xl}.
- Do not use blue SaaS links or gradients when {colors.link} and {colors.primary} are the brand actions.
- Do not add glassmorphism to normal cards; observed surfaces are opaque and border-defined.
- Do not make every card elevated with large drop shadows; use flat panels unless a floating menu requires depth.
- Do not replace code/product modules with generic abstract illustrations.
- Do not over-bold headings; Supabase hierarchy is mostly scale, spacing, and contrast.
- Do not put long marketing copy inside dense dashboard components; product chrome should stay scannable.

**Responsive Behavior**

| Breakpoint | Width | Behavior |
| --- | ---: | --- |
| Mobile | 0px | Single-column content, collapsed nav, stacked pricing plans, full-width buttons. |
| Large mobile | 520px | Headlines reduce to readable 29-32px ranges; cards keep 16px padding. |
| Tablet | 720px | Feature grids can become two columns; hero media remains below text if cramped. |
| Desktop | 960px | Marketing nav and multi-column product sections appear; headings scale upward. |
| Wide | 1280px | Docs sidebars, TOC, wide screenshots, and pricing comparison tables are fully active. |
| Max content | 1536px | Images may bleed wider than article text, but containers stay centered. |

Touch targets should stay at least 34px high for compact controls and 44px high for primary mobile CTAs. Supabase often uses small desktop buttons, but mobile should increase hit area without changing the visual radius.

Collapsing strategy:

- Convert navigation into an icon-triggered menu while preserving muted link hierarchy.
- Stack product cards into one column and preserve borders between modules.
- Place dashboard screenshots below hero copy, then crop or scale them to keep real UI legible.
- Turn comparison tables into mobile row cards with labels in the left column and values on the right.
- Hide secondary docs sidebars before reducing article text size.

Images and product media should use responsive `object-fit: contain` behavior. Screenshots may bleed beyond the text column on desktop, but on mobile they should remain inspectable and avoid dark unreadable thumbnails.

**Iteration Guide**

1. Check the canvas first: the page should read as {colors.canvas} with layered {colors.surfaceAlt}, not a generic black page or a light SaaS layout.
2. Audit action color use: every {colors.primary} element should be actionable, active, semantic-success, or a deliberate brand highlight.
3. Inspect borders: cards, inputs, nav, pricing tables, and docs panes should use {colors.border}; important frames can use {colors.borderStrong}.
4. Verify typography: hero headlines should use regular-weight {typography.hero}, while labels/code must switch to {typography.label} or {typography.code}.
5. Review radii: normal controls should cluster around {rounded.md}; large containers can use {rounded.lg} or {rounded.xl}; avoid extra-soft corners.
6. Confirm product specificity: at least one dashboard frame, table, code panel, or pricing calculator pattern should appear on product-like pages.
7. Test mobile collapse: pricing and docs content should become stacked and readable without hiding primary actions.
8. Remove decorative excess: if a screen relies on generic gradients, big shadows, or abstract shapes instead of product UI, it is drifting away from Supabase.

**Known Gaps**

Observed directly: homepage, `/database`, `/pricing`, and a database docs page were fetched on 2026-05-19. CSS assets exposed the brand green scale, dark/light token variables, font-face declarations for `custom-font`, Source Code Pro usage, Tailwind text scales, radii, border tokens, button classes, form classes, docs sidebars, pricing tables, and code block styling.

Derived: exact component naming in this file is normalized into DESIGN.md roles, so names such as {components.dashboard-frame} and {components.pricing-card} describe recurring patterns rather than exported Supabase component names. Some hex values are converted from observed HSL variables and rounded to practical design-token hex values.

Uncertain: the proprietary `custom-font` appears in CSS but is not publicly named beyond that family label. Marketing pages sometimes use campaign-specific launch gradients and glows; those were treated as episodic accents, not core system defaults. Light mode exists in the token set, but this extraction prioritizes the dark public-site and docs experience because it is the dominant visual signature.
