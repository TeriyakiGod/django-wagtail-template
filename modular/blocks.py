from wagtail import blocks
from wagtailmarkdown import blocks as markdown_blocks

from . import constants


class MarkdownSectionBlock(blocks.StructBlock):
    content = markdown_blocks.MarkdownBlock()
    bg_color = blocks.ChoiceBlock(
        choices=constants.BACKGROUND_COLORS, default="bg-body"
    )
    text_color = blocks.ChoiceBlock(choices=constants.TEXT_COLORS, default="text-body")

    class Meta:
        label = "Markdown Section"
        template = "modular/blocks/markdown_section.html"


class HTMLSectionBlock(blocks.StructBlock):
    content = blocks.RawHTMLBlock()
    bg_color = blocks.ChoiceBlock(
        choices=constants.BACKGROUND_COLORS, default="bg-body"
    )
    text_color = blocks.ChoiceBlock(choices=constants.TEXT_COLORS, default="text-body")

    class Meta:
        label = "HTML Section"
        template = "modular/blocks/html_section.html"


class RichTextSectionBlock(blocks.StructBlock):
    content = blocks.RichTextBlock()
    bg_color = blocks.ChoiceBlock(
        choices=constants.BACKGROUND_COLORS, default="bg-body"
    )
    text_color = blocks.ChoiceBlock(choices=constants.TEXT_COLORS, default="text-body")

    class Meta:
        label = "Rich Text Section"
        template = "modular/blocks/richtext_section.html"
