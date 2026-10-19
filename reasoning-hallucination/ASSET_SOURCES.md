# Project page assets

The affiliations and scientific content follow `01_Manuscript.pdf` and the
supplied S1-S7 release. Logos identify author affiliations, not endorsement.
They are stored locally without redrawing or recoloring the marks. The page
clips accompanying wordmarks with SVG viewports, retaining only each emblem.
Every emblem is centered in a 64-by-64 display box with a 56-unit maximum
content dimension. Mobile sizes scale the entire box proportionally, without
stretching the original mark.

| Affiliation | Asset source |
| --- | --- |
| Zhejiang University | [University logo collection](https://cdn.urongda.com/images/normal/medium/zhejiang-university-logo-1024px.png) |
| Binjiang Institute of Zhejiang University | [Official institute header](http://ibj.zju.edu.cn/uploads/allimg/20230925/1-230925110509350.png) |
| Guangzhou University | [University logo collection](https://cdn.urongda.com/images/normal/medium/guangzhou-university-logo-1024px.png), checked against the [university identity page](https://www.gzhu.edu.cn/xxgk/xxxhxg.htm) |
| Rensselaer Polytechnic Institute | [Official archives seal](https://archives.rpi.edu/sites/default/files/old-wp-content/uploads/2011/03/seal.jpg), documented in [Respect the Seal](https://archives.rpi.edu/blog/2011/03/16/respect-the-seal) |
| The University of Hong Kong | Official header image from [hku.hk](https://www.hku.hk/) |
| HKUST (Guangzhou) | [Official website icon](https://material.hkust-gz.edu.cn/wp-content/uploads/2023/04/cropped-favicon-1-1-192x192.png) |
| The Hong Kong Polytechnic University | [Official header logo](https://www.polyu.edu.hk/assets/img/main-logo-1x.png) |
| Zhejiang Lab | Organization mark from the [official GitHub organization](https://github.com/zhejianglab) |

`tools/fetch_assets.py` and `tools/fetch_template_assets.py` record exact
download URLs. The original research
figures come from the supplied manuscript and supplement. The new survey tree
is exported by `tools/build_page_assets.py` from the hierarchy in `index.html`.
It is an organizational visualization, not a new empirical result.

The interface uses Font Awesome Free 6.5.1, cached locally. Its font is under
SIL OFL 1.1, icons under CC BY 4.0, and code under MIT; see
[Font Awesome licensing](https://fontawesome.com/license/free).

The layout is adapted from the [TFlow project page](https://bwr-hhh.github.io/tflow-project-page/):
centered publication metadata, dark resource buttons, a teaser figure, and
sequential Abstract, Highlights, analysis, materials, and citation sections.
Bulma 0.9.4 and the reference page's Google Sans / Noto Sans font choices are
cached locally. The footer retains the template attribution. The scientific
figures, survey tree, text, and downloadable research materials are specific
to this manuscript; no TFlow research content is reused.

The page is a static local project. `project-page-dist` is the matching clean
publication folder; no remote deployment was performed as part of this edit.

## Video overview

`static/videos/reasoning-lifecycle-overview.mp4` is the approved 35-second
English Manim animation from
`../manim-social/output/survey_film/reasoning_lifecycle_survey_35s.mp4`.
The embedded file is copied without re-encoding: 1920 x 1080, 60 fps, H.264,
silent. Its poster is the first frame from that same final render.
The player has native controls, inline mobile playback, and no autoplay.
Optional English captions reproduce the final SRT and are embedded as WebVTT
data so that local-file viewing does not require a server. A text transcript
is available below the player. The source and clean publication folders both
include the video and poster; no external video host is required.
