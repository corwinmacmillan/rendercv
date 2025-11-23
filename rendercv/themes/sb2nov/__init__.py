from typing import Literal

import pydantic
import pydantic_extra_types.color as pydantic_color

import rendercv.themes.options as o

class Colors(o.Colors):
    name: pydantic_color.Color = pydantic.Field(
        default=pydantic_color.Color("rgb(0,0,0)"),
        description=o.color_common_description,
        examples=o.color_common_examples,
    )
    connections: pydantic_color.Color = pydantic.Field(
        default=pydantic_color.Color("rgb(0,0,0)"),
    )
    section_titles: pydantic_color.Color = pydantic.Field(
        default=pydantic_color.Color("rgb(0,0,0)"),
        description=o.color_common_description,
        examples=o.color_common_examples,
    )


class Header(o.Header):
    name_font_family: o.FontFamily = "New Computer Modern"
    connections_font_family: o.FontFamily = "New Computer Modern"


class Links(o.Links):
    underline: bool = True
    use_external_link_icon: bool = False


class Text(o.Text):
    font_family: o.FontFamily = "New Computer Modern"


class SectionTitles(o.SectionTitles):
    font_family: o.FontFamily = "New Computer Modern"
    type: o.SectionTitleType = "with-full-line"


class Highlights(o.Highlights):
    bullet: o.BulletPoint = "◦"


class EducationEntryOptions(o.EducationEntryOptions):
    first_row_template: str = "**INSTITUTION**\n*DEGREE in AREA* || *LOCATION*\n*DATE*"
    first_column_width: str = "1fr"


class NormalEntryOptions(o.NormalEntryOptions):
    first_row_template: str = "**NAME** || *LOCATION*\n*DATE*"


class ExperienceEntryOptions(o.ExperienceEntryOptions):
    first_row_template: str = "**POSITION**\n*COMPANY* || *LOCATION*\n*DATE*"


class EntryOptionsTypes(o.EntryTypes):
    education_entry: EducationEntryOptions = pydantic.Field(
        default_factory=EducationEntryOptions,
    )
    normal_entry: NormalEntryOptions = pydantic.Field(
        default_factory=NormalEntryOptions,
    )
    experience_entry: ExperienceEntryOptions = pydantic.Field(
        default_factory=ExperienceEntryOptions,
    )


class Sb2novThemeOptions(o.ThemeOptions):
    theme: Literal["sb2nov"] = "sb2nov"
    header: Header = pydantic.Field(
        default_factory=Header,
    )
    links: Links = pydantic.Field(
        default_factory=Links,
    )
    text: Text = pydantic.Field(
        default_factory=Text,
    )
    colors: Colors = pydantic.Field(
        default_factory=Colors,
    )
    highlights: Highlights = pydantic.Field(
        default_factory=Highlights,
    )
    entry_types: EntryOptionsTypes = pydantic.Field(
        default_factory=EntryOptionsTypes,
    )
    section_titles: SectionTitles = pydantic.Field(
        default_factory=SectionTitles,
    )