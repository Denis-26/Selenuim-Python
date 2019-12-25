from base_page import BasePage


class SearchResultsPage(BasePage):

    def is_results_found(self):
        return "No results found." not in self.driver.page_source
