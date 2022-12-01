+++
# A Demo section created with the Blank widget.
# Any elements can be added in the body: https://sourcethemes.com/academic/docs/writing-markdown-latex/
# Add more sections by duplicating this file and customizing to your requirements.

widget = "blank"  # See https://sourcethemes.com/academic/docs/page-builder/
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 20  # Order that this section will appear.

title = ""
subtitle = ""

[design]
  # Choose how many columns the section has. Valid values: 1 or 2.
  columns = "1"

[design.spacing]
  # Customize the section spacing. Order is top, right, bottom, left.
  padding = ["20px", "0", "20px", "0"]

[advanced]
 # Custom CSS.
 css_style = ""
@import "compass/css3";

/**
 * Use the :target pseudo-element to apply
 * styles to the element with the same ID as  
 * the fragment identifier.
 * (e.g. `#bib-author2000paper`)
 * 
 * The pseudo-element can also be used in
 * conjunction with another selector to 
 * define a variety of target styles.
 * (e.g. `#target-section:target)
 */

:bib {
	-webkit-animation: target-fade 1s;
	-moz-animation: target-fade 1s;
	-o-animation: target-fade 1s;
	animation: target-fade 1s;
}


/**
 * Keyframe animation definition
 * 
 * 1. Insert a color of your choice here
 */

@-webkit-keyframes target-fade {
	from { background-color: red; } /* [1] */
	to { background-color: transparent; }
}

@-moz-keyframes target-fade {
	from { background-color: red; } /* [1] */
	to { background-color: transparent; }
}

@-o-keyframes target-fade {
	from { background-color: red; } /* [1] */
	to { background-color: transparent; }
}

@keyframes target-fade {
	from { background-color: red; } /* [1] */
	to { background-color: transparent; }
}
""

 # CSS class.
 css_class = ""


+++

{{< bibliography >}}