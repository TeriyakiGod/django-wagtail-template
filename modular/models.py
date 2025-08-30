from wagtail import fields
from wagtail.admin import panels
from wagtail.models import Page

from . import blocks


class ModularPage(Page):
    body = fields.StreamField(
        [
            ("markdown_section", blocks.MarkdownSectionBlock()),
            ("html_section", blocks.HTMLSectionBlock()),
            ("richtext_section", blocks.RichTextSectionBlock()),
        ],
        blank=True,
    )

    content_panels = Page.content_panels + [
        panels.FieldPanel("body"),
    ]
