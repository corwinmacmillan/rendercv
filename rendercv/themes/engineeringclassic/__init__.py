from typing import Literal

import rendercv.themes.options as o


class Page(o.Page):
    show_page_numbering: bool = False


class Header(o.Header):
    name_font_family: o.FontFamily = "Raleway"
    name_bold: bool = False
    alignment: o.Alignment = "left"
    connections_font_family: o.FontFamily = "Raleway"


class Links(o.Links):
    use_external_link_icon: bool = False


class Text(o.Text):
    font_family: o.FontFamily = "Raleway"


class SectionTitles(o.SectionTitles):
    font_family: o.FontFamily = "Raleway"
    bold: bool = False


class Highlights(o.Highlights):
    left_margin: o.TypstDimension = "0cm"



class EducationEntryOptions(o.EducationEntryOptions):
    first_row_template: str =  "**INSTITUTION**, AREA -- LOCATION || DATE"
    first_column_width: str = "1fr"


class NormalEntryOptions(o.NormalEntryOptions):
    first_row_template: str = "**NAME** -- **LOCATION** || DATE"


class ExperienceEntryOptions(o.ExperienceEntryOptions):
    first_row_template: str = "**POSITION**, COMPANY -- LOCATION || DATE"


class EntryOptionsTypes(o.EntryTypes):
    education_entry: EducationEntryOptions = EducationEntryOptions()
    normal_entry: NormalEntryOptions = NormalEntryOptions()
    experience_entry: ExperienceEntryOptions = ExperienceEntryOptions()


class EngineeringclassicThemeOptions(o.ThemeOptions):
    theme: Literal["engineeringclassic"] = "engineeringclassic"
    page: Page = Page()
    header: Header = Header()
    highlights: Highlights = Highlights()
    text: Text = Text()
    links: Links = Links()
    entry_types: EntryOptionsTypes = EntryOptionsTypes()
    section_titles: SectionTitles = SectionTitles()
