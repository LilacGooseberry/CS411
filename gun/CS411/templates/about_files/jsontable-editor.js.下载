// Todo - COPYRIGHT 
/*jshint esversion: 6 */
'use strict';

AJS.bind("init.rte", function(evt) {

    console.log("appfire: event=" + evt.type + "; macro name=json-table");
    
    (function ($) {
    //json-table Specific params here
    //total param count=46
    const jsontableParms = {
            paths: "",
            fieldPaths: "",
            fieldOrderRegexPatterns: "",
            sortPaths: "",
            stripQualifiers: false,
            capitalize: true,
            output: "html",
            columns: "",
            script: "",
            url: "",
            user: "",
            password: "",
            timeout: "",
            encoding: "",
            showWiki: false,
            escape: false,
            macros: false,
            augments: "",
            headingAugments: "",
            footingAugments: "",
            autoNumberSort: false,
            footing: 0, 
            heading: 1,
            border: "",
            width: "",
            disableAntiXss: false
    }
    
    var jsontableAllParms = $.extend({}, tablebasecme.commonTableParams, jsontableParms );
    appcme.setMacroJsOverride('json-table', jsontableAllParms, function(macroDetails) {

        // merge specific ones with jsontableAllParms.
        var parms = appcme.parametersToObj(jsontableAllParms, macroDetails.params, tablebasecme.DELIMITER, tablebasecme.QUOTE);
        $.extend(parms, {macroName: macroDetails.name, macroBody: (macroDetails.body ? macroDetails.body.trim() : ''), dataTypeToLocate: 'JSON'}); //NTBL-79:macroBody needed to indicate if data source is macroBody, if it contains data
        parms = tablebasecme.splitScriptParam(parms);
        
        return {
            icon: "/download/resources/org.swift.confluence.table/img/table-32x32.png",
            title: "Advanced Table Editor - JSON Table",
            showPreview: true,
            dataAttributes: {commontableeditor: "true", datalocationfields: "true"}, // required for all apps built around the common table editors for common event
            navigation: {
                primary: [
                    {
                        icon: appcme.absolutePath("/download/resources/org.swift.confluence.table/editor-img/icon-nav-json-48-wht-on-clr.png"),
                        name: "JSON settings",
                        panel: org.swift.confluence.table.jsontable.editor.jsontableSettingsPanel(parms)
                    },
                    {
                        icon: appcme.absolutePath("/download/resources/org.swift.confluence.tablesorter/table-editor/img/icon-nav-table-48-wht-on-clr.png"),
                        name: "Table settings",
                        panel: org.swift.confluence.table.editor.tableSettingsPanel(parms)
                    },
                    {
                        icon: appcme.absolutePath("/download/resources/org.swift.confluence.tablesorter/table-editor/img/icon-nav-columns-48-wht-on-clr.png"),
                        name: "Column settings",
                        panel: org.swift.confluence.table.editor.columnSettingsPanel(parms)
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
                        name: "JSON Table guide",
                        url: "https://bobswift.atlassian.net/wiki/x/o4B8M" 
                    },
                    {
                        icon: appcme.absolutePath("/download/resources/org.swift.confluence.tablesorter/editor/img/icon-nav-docs-48-wht-on-clr.png"),
                        name: "JSON Table Documentation",
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
                tablebasecme.validateDataLocationFields(dialog, errors);
                return tablebasecme.validateCommonTableParams(dialog, errors);
            }
        };
    });
    }(AJS.$));
});
