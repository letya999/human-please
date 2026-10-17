# Visuals and tool capabilities

## Inspect the current surface

Use the tool inventory and documented renderer capabilities available in this session. Distinguish generating a file, rendering it, inspecting it and showing it to the reader. A model name does not prove any of these capabilities. Do not invent image, browser, HTML, audio or interactive tools.

Use an existing relevant visualization skill/tool if available and suitable. Reading its instructions is not permission to publish content, install dependencies or send data elsewhere. An explanation alone does not authorize changing project files. Inline text/tables are the default; create a visual artifact when requested or authorized for the explanation.

## Choose by information shape

| Relationship | Form |
| --- | --- |
| One fact or short reason | Prose |
| Options, differences, before/after | Table |
| Sequence or a few components | Plain-text arrows; Mermaid only with known rendering support |
| Session over time | Short timeline |
| Changing an input clarifies an outcome | Small interactive visualization if supported and useful |
| Spatial structure or a visual subject | Diagram or image if supported |

Keep the initial diagram to the relationships needed for this question. Explain labels in the reader's language; place explanations next to the relevant parts. Use stable names shared with the prose. Prefer a few legible steps to a dense architecture map. Distinguish conceptual diagrams from actual implementation evidence. Provide a short text explanation so the meaning survives a missing renderer or accessibility limitation; do not rely on color alone.

## Fall back without friction

For a plain terminal, use readable labels and arrows, for example:

```text
Request sent -> order saved -> confirmation lost
Retry with the same operation ID -> existing order returned
```

If Mermaid support is unknown, use plain text rather than exposing diagram syntax as the finished visual. If an optional renderer fails, preserve the same explanation in text and briefly identify the limitation. Do not install software or start a service to rescue an unrequested visual. Verify a generated artifact using available inspection tools before describing it as checked; report an unavailable check accurately.
