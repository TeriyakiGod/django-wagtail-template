from wagtail import fields
from wagtail.admin import panels
from wagtail.models import Page

from . import blocks


class ModularPage(Page):
    content = fields.StreamField(
        [
            ("section", blocks.SectionBlock()),
        ],
        blank=True,
    )

    content_panels = Page.content_panels + [
        panels.FieldPanel("content"),
    ]
