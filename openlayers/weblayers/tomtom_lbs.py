# -*- coding: utf-8 -*-
"""
/***************************************************************************
OpenLayers Plugin
A QGIS plugin

                             -------------------
begin                : 2009-11-30
copyright            : (C) 2009 by Pirmin Kalberer, Sourcepole
email                : pka at sourcepole.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from weblayer import WebLayer3857


class TomTomLbsLayer(WebLayer3857):

    emitsLoadEnd = True

    def __init__(self, name, html, icon):
        WebLayer3857.__init__(self, groupName="TomTom LBS", groupIcon=icon,
                              name=name, html=html)

class TomTomLbsBaseLayer(TomTomLbsLayer):

    def __init__(self):
        TomTomLbsLayer.__init__(self, name='TomTom Base layer', html='tomtom_base.html', icon='tomtom_icon.png')

class TomTomLbsHDTrafficLayer(TomTomLbsLayer):

    def __init__(self):
        TomTomLbsLayer.__init__(self, name='TomTom HDTraffic layer', html='tomtom_traffic.html', icon='tomtom_hdtraffic_icon.png')