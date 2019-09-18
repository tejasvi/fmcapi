from fmcapi.api_objects.classtemplates import APIClassTemplate
import logging
import warnings


class URLCategories(APIClassTemplate):
    """
    The URLCategories Object in the FMC.
    """

    url_suffix = '/object/urlcategories'
    valid_characters_for_name = """[.\w\d_\-\/\.\(\) ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for URLCategories class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for URLCategories class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for URLCategories class.")

    def post(self):
        logging.info('POST method for API for URLCategories not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for URLCategories not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for URLCategories not supported.')
        pass


class URLCategory(URLCategories):
    """Dispose of this Class after 20210101."""

    def __init__(self, fmc, **kwargs):
        warnings.resetwarnings()
        warnings.warn("Deprecated: URLCategory() should be called via URLCategories().")
        super().__init__(fmc, **kwargs)
