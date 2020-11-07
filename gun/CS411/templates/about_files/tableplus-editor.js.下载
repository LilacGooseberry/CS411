// Todo - COPYRIGHT 
/*jshint esversion: 6 */
'use strict';

AJS.bind("init.rte", function(evt) {

    console.log("appfire: event=" + evt.type + "; macro name=table-plus"); 
    
    (function ($) {
    //table-plus specific macro params
    //Total param count=26
    const tableplusParms = {
        autoNumberSort: false, 
        footing: 0,  
        heading: 1, 
        border: "",
        width: "",
        multiple: true
    };
    
    var tableplusAllParms = $.extend({}, tablebasecme.commonTableParams, tableplusParms );
    appcme.setMacroJsOverride('table-plus', tableplusAllParms, function(macroDetails) {

        // merge specific ones with tableplusAllParms.
        var parms = appcme.parametersToObj(tableplusAllParms, macroDetails.params, tablebasecme.DELIMITER, tablebasecme.QUOTE);
        $.extend(parms, {macroName: macroDetails.name}); 
        
        return {
            icon: "/download/resources/org.swift.confluence.table/img/table-32x32.png",
            title: "Advanced Tables Editor - Table Plus",
            showPreview: true,
            dataAttributes: {commontableeditor: "true"}, // required for all apps built around the common table editors for common events
            navigation: {
                primary: [
                    {
                        icon: appcme.absolutePath("/download/resources/org.swift.confluence.tablesorter/table-editor/img/icon-nav-table-48-wht-on-clr.png"),
                        name: "Table settings",
                        panel: org.swift.confluence.table.editor.tableSettingsPanel(parms)
                    },
                    {
                        icon: appcme.absolutePath("/download/resources/org.swift.confluence.tablesorter/table-editor/img/icon-nav-columns-48-wht-on-clr.png"),
                        name: "Column settings",
                        panel: org.swift.confluence.table.editor.columnSettingsPanel(parms),
                        /* Table Plus has the Column settings tab be the first tab when editor is opened.  */
                        activePanel: true 
                    },
                    {
                        icon: appcme.absolutePath("/download/resources/org.swift.confluence.tablesorter/table-editor/img/icon-nav-rows-48-wht-on-clr.png"),
                        name: "Row formatting",
                        panel: org.swift.confluence.table.editor.rowSettingsPanel(parms)
                    }
                ],
                secondary: [
                    {
                        icon: appcme.absolutePath("/download/resources/org.swift.confluence.tablesorter/editor/img/icon-nav-guide-48-wht-on-clr.png"),
                        name: "Table Plus guide",
                        url: "https://bobswift.atlassian.net/wiki/x/GoD7MQ"
                    },
                    {
                        icon: appcme.absolutePath("/download/resources/org.swift.confluence.tablesorter/editor/img/icon-nav-docs-48-wht-on-clr.png"),
                        name: "Table Plus Documentation",
                        url: "https://bobswift.atlassian.net/wiki/x/jIADLQ" 
                    }
                ]
            },
            /**
             * Validate form fields. 
             * Input Parameters:
             *      dialog - The jQuery editor dialog 
             *      form - The jQuery form from the dialog 
             * Return Parameters:
             *      errors - This is a property array.  Each array element contains the message and an optinal jQuery element for the error.  
             * Return: 
             *      True if the form validates correctly and can be saved. False if there are any errors. The form will not be allowed to close in that case. 
             */
            validator: function (dialog, form, errors) {
                return tablebasecme.validateCommonTableParams(dialog, errors);
            }
        };
    });
    }(AJS.$));
});
