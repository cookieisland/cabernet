"""
MIT License

Copyright (C) 2023 ROCKY4546
https://github.com/rocky4546

This file is part of Cabernet

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the “Software”), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.
"""

from lib.common.decorators import getrequest


@getrequest.route('/api/plugins')
def get_plugins_html(_webserver):
    plugins_html = PluginsHTML()
    html = plugins_html.get()
    _webserver.do_mime_response(200, 'text/html', html)


class PluginsHTML:

    def __init__(self):
        self.config = None
        self.active_tab_name = None
        self.tab_names = None

    def get(self):
        self.tab_names = self.get_tabs()
        return ''.join([self.header, self.body])

    @property
    def header(self):
        return ''.join([
            '<!DOCTYPE html><html><head>',
            '<meta charset="utf-8"/><meta name="author" content="rocky4546">',
            '<meta name="description" content="Cabernet Plugins">',
            '<title>Plugins</title>',
            '<meta name="viewport" content="width=device-width, ',
            'minimum-scale=1.0, maximum-scale=1.0">',
            '<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>',
            '<link rel="stylesheet" type="text/css" href="/modules/tabs/tabs.css">',
            '<link rel="stylesheet" type="text/css" href="/modules/table/table.css">',
            '<script src="/modules/tabs/tabs.js"></script>',
            '<script src="/modules/channels/channels.js"></script></head>'
        ])

    @property
    def title(self):
        return ''.join([
            '<body><div class="container">',
            '<h2>Plugins</h2>'
        ])

    @property
    def tabs(self):
        activeTab = 'activeTab'
        tabs_html = ''.join([
            '<ul class="tabs">'])
        for name, icon in self.tab_names.items():
            key = name.replace(' ', '_')
            tabs_html = ''.join([
                tabs_html,
                '<li><a id="tab', name, '" class="form',
                name, ' configTab ',
                activeTab,
                '" href="#" onclick=\'load_form_url("/api/pluginsform?name=',
                key, '")\'>',
                '<i class="md-icon tabIcon">',
                icon,
                '</i>',
                name, '</a></li>'
            ])
            activeTab = ''
            self.active_tab_name = name
        tabs_html = ''.join([tabs_html, '</ul>'])
        return tabs_html

    @property
    def body(self):
        return ''.join([
            self.title,
            self.tabs,
            '<div id="tablecontent"><script>load_form_url("/api/pluginsform?name=My_Plugins")</script></div>'
        ])

    def get_tabs(self):
        return {'My Plugins': 'extension', 'Catalog': 'add_shopping_cart'}
