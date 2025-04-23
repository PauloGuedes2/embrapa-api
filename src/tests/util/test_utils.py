import pytest
from bs4 import BeautifulSoup

from domain.enum.enums import ImportSubOption, ExportSubOption, ProcessingSubOption
from util.utils import Utils


class TestUtils:
    def test_extract_generic_table_data_success(self):
        html = """
                <table class="test-table">
                    <tr><th>Header</th></tr>
                    <tr><td>Row1</td></tr>
                    <tr><td>Row2</td></tr>
                </table>
                """
        soup = BeautifulSoup(html, 'html.parser')
        result = Utils.extract_generic_table_data(soup, "test-table", 1)
        assert result == [["Row1"], ["Row2"]]

    def test_extract_generic_table_data_with_transformer(self):
        html = """
                <table class="test-table">
                    <tr><th>Header</th></tr>
                    <tr><td>Row1</td></tr>
                </table>
                """
        soup = BeautifulSoup(html, 'html.parser')
        transformer = lambda x: [item.upper() for item in x]
        result = Utils.extract_generic_table_data(soup, "test-table", 1, transformer)
        assert result == [["ROW1"]]

    def test_extract_generic_table_data_table_not_found(self):
        soup = BeautifulSoup("<div></div>", 'html.parser')
        with pytest.raises(ValueError, match="Table with class 'missing-table' not found"):
            Utils.extract_generic_table_data(soup, "missing-table", 0)

    def test_build_url_with_year_only(self):
        result = Utils.build_url("http://example.com/data", year=2023)
        assert result == "http://example.com/data?ano=2023"

    def test_build_url_with_suboption_only(self):
        result = Utils.build_url("http://example.com/data", sub_option=ImportSubOption.subopt_01)
        assert result == "http://example.com/data?subopcao=subopt_01"

    def test_build_url_with_year_and_suboption(self):
        result = Utils.build_url(
            "http://example.com/data?existing=param",
            year=2023,
            sub_option=ExportSubOption.subopt_02
        )
        assert result == "http://example.com/data?existing=param&ano=2023&subopcao=subopt_02"

    def test_build_url_with_custom_param_names(self):
        result = Utils.build_url(
            "http://example.com/data",
            year=2023,
            sub_option=ProcessingSubOption.subopt_03,
            year_query_param="year",
            suboption_query_param="option"
        )
        assert result == "http://example.com/data?year=2023&option=subopt_03"

    def test_build_url_with_invalid_suboption_type(self):
        with pytest.raises(ValueError, match="Import URL requires ImportSubOption"):
            Utils.build_url("http://example.com/data?opcao=opt_05", sub_option=ExportSubOption.subopt_01)

    def test_build_url_no_params(self):
        result = Utils.build_url("http://example.com/data")
        assert result == "http://example.com/data"
