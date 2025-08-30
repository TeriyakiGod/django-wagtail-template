from wagtail import blocks
from wagtailmarkdown import blocks as markdown_blocks

from . import constants


class SectionBlock(blocks.StructBlock):
    content = markdown_blocks.MarkdownBlock()
    bg_color = blocks.ChoiceBlock(
        choices=constants.BACKGROUND_COLORS, default="bg-primary"
    )
