from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings import models as settings_models
from wagtail.fields import StreamField


@settings_models.register_setting
class NavigationSettings(settings_models.BaseGenericSetting):
    links = StreamField(
        [
            (
                "link",
                blocks.StructBlock(
                    [
                        (
                            "icon",
                            blocks.CharBlock(
                                required=True, help_text="Icon name or CSS class"
                            ),
                        ),
                        ("name", blocks.CharBlock(required=True)),
                        ("url", blocks.URLBlock(required=True)),
                    ]
                ),
            ),
        ],
        blank=True,
        use_json_field=True,
    )

    panels = [
        FieldPanel("links"),
    ]
