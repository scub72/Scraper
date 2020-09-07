def query_phrase_notation(query):
    """Additional function to help change words notation from ex. 'dog eat dog' to 'dog+eat+dog' """
    return '+'.join(query.split(' '))


class GoogleSearchString:
    """
    Creates search link for Google search website

    PARAMETERS DESCRIPTION

        :const GOOGLE_SEARCH:       the URL for google search engine,
                                    default value = 'http://www.google.com/search?'


        Bounded to the 'q' parameter

        :param query:               query phrase needed to create query string
                                    'q=query+goes+here', words are separated by '+'
        :param allintitle:          appends 'q' and is for searching in the title
                                    'q=fishing+allintitle%3Asea+bass'
                                    default: None
        :param allintext:           same function as allintitle
        :param allinurl:            same function as allintitle
        :param allinanchor:         same function as allintitle
        :param parameter_range:     similar to allin
                                    'nn..yy' for example if want a range from 15 to 100 should be 15..100
        :param only_used_term:      is actually the + sign encoded, and will return results
                                    featuring only the term used, with no pluralisations,
                                    alternate tenses, or synonyms.
                                    '%2Bterm'
                                    default: False
        :param term_and_synonyms:   Returns results for the term used and synonyms.
                                    '~term'
                                    default: False
        :param def_word:            Returns definitions for the word you put in.
                                    'define%3Aword'
                                    default: False
        :param exp_between_words:   Returns results with listings that contain both words,
                                    with other words between them.
                                    'term * term two'
                                    default: None


        Other parameters:

        :param remain_word_order:   if set true the search engine obey the word order
                                    'as_epq=query+goes+here';
                                    default: implemented with basic_query method
        :param chosen_word_order:   search engine obey the order of the words inside quotations marks
                                    'as_oq="query+string"+goes+here'
                                    default: implemented with basic_query method
        :param words_excluded:      results must not include any words in this string
                                    'as_eq=don't+include+these+words'
                                    default: None
        :param results_number:      number of shown results anything up to 100
                                    'num=xx'
                                    default: None
        :param filetype_ext:        the file extension that google searches
                                    'as_filetype=extension'
                                    default: None
        :param site_limit:          limits the results to just the site you choose
                                    'as_sitesearch=example.com'
                                    default: None
        :param files_indexed_time:  Swap out x for the following to limit the search to only files
                                    first indexed in:
                                    'as_qdr=x'
                                        'd' - previous 24 hours
                                        'w' - previous 7 days
                                        'm' - previous month
                                        'y' - past year
                                        'mn' - the previous 'n' number of month so m2 would be the previous two,
                                               m3 would be three, and so on. Does work into double digits
        :param limit_files_pages:   Limits the search to files/pages that have certain rights.
                                    If you want to make up your own, put the bits you want in brackets,
                                    separated by pipe characters (|), and exclude the bits you don't by
                                    putting them in brackets, preceded by .- and again pipe-separated.
                                    'as_rights=xxx'
                                        The options are:
                                        (cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived)
                                            - free to use or share
                                        (cc_publicdomain|cc_attribute|cc_sharealike|cc_nonderived).-(cc_noncommercial)
                                            - free to use or share, including commercially
                                        (cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial).-(cc_nonderived)
                                            - free to use, share, or modify
                                        (cc_publicdomain|cc_attribute|cc_sharealike).-(cc_noncommercial|cc_nonderived)
                                            - free to use, share, or modify commercially

        :param google_calc:         Google's calculator functions. They are, in order, add, subtract,
                                    divide, multiply, raise to the power of, and return x percentage of.
                                    'n+n2, n-n2, n/n2, n*n2, n^n2 and n% of n2'
                                    Not implemented in this class
        :param safe_search:         Sets safe search to on. To turn it off, change active to images.
                                    'safe=active'
                                    default: False
        :param url_related:         Finds sites Google thinks are related to the URL you put in.
                                    'as_rq=example.com'
                                    default: None
        :param sites_link_to_url:   Finds sites that link to the URL you put in.
                                    'as_lq=example.com'
                                    default: None
        :param newwindow:           Opens clicked listings in a new window. Very useful for opening
                                    lots of documents at a time, for competitor research.
                                    Set to 1 to activate, and 0 to turn it off.
                                    'newwindow=n'
                                    default: Not Implemented
        :param personalised_search: Controls whether personalised search is on or not.
                                    Set to 1 to activate, and 0 to turn it off.
                                    'pws=1'
                                    default: False
        :param adtest:              Turns off AdWords database connection, so your browsing won't
                                    show up as an impression, and will disable the URLs.
                                    Set to on to activate, and off to turn it off.
                                    'adtest=on'
                                    default: False
        :param :                    Simulates a click on the normal Google results buttom.
                                    Change to btnI to get the I'm Feeling Lucky button result.
                                    'btnG=Search'
                                    default: Not Implemented
        :param :                    Controls the input encoding settings.
                                    This defaults to UTF-8, and is worked out server-side,
                                    hence changing it doesn't do anything.
                                    'ie='
                                    default: Not Implemented
        :param :                    Controls the output encoding settings.
                                    Works in the same way as ie, so you can tinker away,
                                    but it won't do anything.
                                    'oe='
                                    default: not implemented
        :param interface_lang:      Changes the interface language.
                                    '&hl=value'
                                    default: None
        :param limit_languages:     Limits the languages used to return results.
                                    Not hugely effective.
                                    'lr=value'
                                    default: None
        :param limit_locations:     Limits the search results to pages/sites from certain locations.
                                    Change XX to any of the following, to limit the results:
                                    'cr=countryXX'
                                    default: None
        :param omitted_res_filter:   Eliminates the "omitted results" or "similar results" filter,
                                    and allows all results to show in the SERP.
                                    '&filter=0'
                                    default: False
    """
    GOOGLE_SEARCH = 'http://www.google.com/search?'

    allintitle = None #ok
    allintext = None #ok
    allinurl = None #ok
    allinanchor = None #ok
    parameter_range = None #ok
    only_used_term = False #ok
    term_and_synonyms = False #ok
    def_word = False #ok

    exp_between_words = None
    obey_word_order = False #ok
    chosen_word_order = False #ok
    words_excluded = None #ok
    results_number = None #ok
    filetype_ext = None #ok
    site_limit = None #ok
    files_indexed_time = None #ok
    limit_files_pages = None #ok
    safe_search = False #ok
    url_related = None #ok
    sites_link_to_url = None #ok
    personalised_search = False #ok
    adtest = False #ok
    interface_lang = None #ok
    limit_languages = None #ok
    limit_locations = None #ok
    omitted_res_filter = False #ok

    search_url = None

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def search_query(self, query):
        """Forms complete query"""
        if query is not "":
            self.search_url = self.GOOGLE_SEARCH \
                              + self.basic_query_prefix_options() \
                              + self.basic_query(query) \
                              + self.basic_query_append_options() \
                              + self.advanced_search_options()
            return self.search_url

        if query is "" & ((self.basic_query_prefix_options() is not "")|(self.basic_query_append_options() is not "")):
            self.search_url = self.GOOGLE_SEARCH \
                              + self.basic_query_prefix_options() \
                              + self.basic_query(query) \
                              + self.basic_query_append_options() \
                              + self.advanced_search_options()
            return self.search_url

        else:
            print(Exception('Empty query.'))

    def basic_query_prefix_options(self):
        """Adds options after 'q=' parameter and before query """
        if self.only_used_term:
            return '%2Bterm'
        if self.term_and_synonyms:
            return '~term'
        if self.def_word:
            return 'define%3A'
        else:
            return ""

    def basic_query_append_options(self):
        """Adds options after query, before additional parameters """
        query_append = ""
        if self.allintitle is not None:
            query_append = query_append + '+allintitle%3A' + query_phrase_notation(self.allintitle.__str__())
        elif self.allintext is not None:
            query_append = query_append + '+allintext%3A' + query_phrase_notation(self.allintext.__str__())
        elif self.allinurl is not None:
            query_append = query_append + '+allinurl%3A' + query_phrase_notation(self.allinurl.__str__())
        elif self.allinanchor is not None:
            query_append = query_append + '+allinanchor%3A' + query_phrase_notation(self.allinanchor.__str__())
        elif self.parameter_range is not None:
            query_append = query_append + self.parameter_range.__str__()

        return query_append

    def basic_query(self, query):
        """
        Analyzes the simple searching query and form the basic search phrase.

        :param query:       the query phrase like one written in the browser
                            example queries: 'my big dog'; '"my big" dog'; '"my big dog"'
        :return reg expr:   simple query phrase to send to browser
        """

        if query.endswith('"') & query.startswith('"'):
            self.obey_word_order = True
            return 'as_epq=' + query_phrase_notation(query.replace('"', ''))
        elif '"' in query:
            self.chosen_word_order = True
            return 'q=' + query_phrase_notation(query) + '&oq=' + query_phrase_notation(query)
        else:
            return 'q=' + query_phrase_notation(query)

    # def add_to_url(self, option):
    #     """Adds advanced options string to simple generated url"""
    #     self.search_url = self.search_url + option

    def check_month_count(self):
        """Checks if the parameter of file_indexed_time is correctly defined"""
        if self.files_indexed_time.startswith('m') & (self.files_indexed_time.__len__() > 1):
            try:
                int(self.files_indexed_time.__str__().lstrip('m'))
                return True
            except ValueError:
                print("Parameter error. Pattern is 'mxx' where 'xx' should be numerical")
                return False

    def advanced_search_options(self):
        """Inspects if there are any additional options for searching"""
        options = ""
        if self.words_excluded is not None:
            options = options + '&as_eq=' + query_phrase_notation(self.words_excluded.__str__())

        elif self.results_number is not None:
            if 0 < self.results_number <= 100:
                options = options + '&num='+self.results_number.__str__()
            else:
                print('Wrong results number. shold be in range 1-100')

        elif self.filetype_ext is not None:
            options = options + '&as_filetype=' + self.filetype_ext.__str__()

        elif self.site_limit is not None:
            options = options + '&as_sitesearch=' + self.site_limit.__str__()

        elif self.files_indexed_time is not None:
            if (self.files_indexed_time in ('d', 'w', 'm', 'y')) | self.check_month_count():
                options = options + '&as_qdr=' + self.files_indexed_time.__str__()
            else:
                print('Parameter is defined wrong,  please check documentation')

        elif self.limit_files_pages is not None:
            options = options + '&as_rights=' + self.limit_files_pages.__str__()

        elif self.safe_search:
            options = options + '&safe=active'

        elif self.url_related is not None:
            options = options + '&as_rq=' + self.url_related.__str__()

        elif self.sites_link_to_url is not None:
            options = options + '&as_lq=' + self.sites_link_to_url.__str__()

        elif self.personalised_search:
            options = options + '&pws=1'

        elif self.adtest:
            options = options + '&adtest=on'

        elif self.interface_lang is not None:
            options = options + '&hl=' + self.interface_lang.__str__()

        elif self.limit_languages is not None:
            options = options + '&lr=' + self.limit_languages.__str__()

        elif self.limit_locations is not None:
            options = options + '&cr=country' + self.limit_locations.__str__()

        elif self.omitted_res_filter:
            options = options + '&filter=0'

        return options
