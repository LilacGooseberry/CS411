/*
 * Copyright (c) 2019 Appfire Technologies, Inc.
 * All rights reserved.
 *
 * This software is licensed under the provisions of the "Bob Swift Atlassian Add-ons EULA"
 * (https://bobswift.atlassian.net/wiki/x/WoDXBQ) as well as under the provisions of
 * the "Standard EULA" from the "Atlassian Marketplace Terms of Use" as a "Marketplace Product"
 * (http://www.atlassian.com/licensing/marketplace/termsofuse).
 *
 * See the LICENSE file for more details.
 */
/*jshint esversion: 6 */
'use strict';

$(document).on('appfireEditorBeforeSerialize appfireEditorBeforePreviewSerialize', "[data-appfire-macro-name='attachment-table']", 
        function(evt, dialog, form, defaultParms, errors) {
        //set data-atalocationfields false, so that the common handlers wont be called for attachment-table macro. 
        $(this).attr("data-datalocationfields", "false");
});


$(document).on('appfireEditorBeforeSave appfireEditorBeforePreview', "[data-appfire-macro-name='attachment-table']", function(evt, macroParms, dialog, form, defaultParms, macroName) {
    
    console.log("appfire: event=" + evt.type + "; macro name=" + $(evt.target).closest("[data-appfire-macro-name]").data("appfireMacroName"));
    //construct attachmentPage param back from splitted params and remove the non macro params
    var attachmentSource = dialog.find("#attachmentSource").val();
    if (attachmentSource === "attachment"){
        var space = macroParms["attSpace"];
        var page = macroParms["attPage"];
        if(tablebasecme.specialPageValues.hasOwnProperty(page.toLowerCase())) {
            if ("@self" == page.toLowerCase()) {
                delete macroParms["attachmentPage"];
            } else {
                macroParms["attachmentPage"] = page;
            }
        }
        else{
            if(space !== tablebasecme.CURRENT_SPACE){
                macroParms["attachmentPage"] = space + ":" + page
            }
            else{//if current space
                //if current page, then need not save space or page to be backward compatible    
                if(page === tablebasecme.CURRENT_PAGE){
                    delete macroParms["attachmentPage"];
                }
                else{
                   //if current space but different page, then just save 'page' to be backward compatible   
                    macroParms["attachmentPage"] = page; 
                }
            }
        }

        //singlepage selected, hence remove spaceregex and pageregex. Checked behavior in marketplace version
        delete macroParms["spaceRegex"];
        delete macroParms["pageRegex"];
    }
    delete macroParms["attSpace"];
    delete macroParms["attPage"];
    delete macroParms["attachmentSource"];
});

AJS.bind("init.rte", function(evt) {

    console.log("appfire: event=" + evt.type + "; macro name=attachment-table"); 
    
    (function ($) {
    //attachment-table Specific params here
    //Total param count=33
    const attachmenttableParms = {
            attachmentPage: "",
            spaceRegex: "",
            includePersonalSpaces: false,
            pageRegex: "",
            pageLabelRegex: "",
            attachmentRegex: "",
            commentRegex: "",
            labelRegex: "",
            labelMatchOption: "any",
            textForNone: "",
            dateFormat: AJS.Meta.get('date.format'),
            limit: 1000,
            columns: "",
    }
    
    var attachmenttableAllParms = $.extend({}, tablebasecme.commonTableParams, attachmenttableParms );
    appcme.setMacroJsOverride('attachment-table', attachmenttableAllParms, function(macroDetails) {

        // merge specific ones with attachmenttableAllParms.
        var parms = appcme.parametersToObj(attachmenttableAllParms, macroDetails.params, tablebasecme.DELIMITER, tablebasecme.QUOTE);
        $.extend(parms, {macroName: macroDetails.name}); 
        var page = parms.attachmentPage;
        var spaceKey;
        var pageTitle;
        if(page){
            //page is any of @self, @page or @parent, then default to current space
            if(tablebasecme.specialPageValues.hasOwnProperty(page.toLowerCase().trim())){
                 //Do not set current space by default
                pageTitle = page;
            }
            else{
              //if page param contains space:page name, then choose space default space
                if(page.indexOf(":") > 0){
                    spaceKey = page.substring(0, page.indexOf(":"));
                    pageTitle = page.substring(page.indexOf(":")+1, page.length);
                }
                else{
                    //if page param contains just page name, then choose space default space
                    spaceKey = tablebasecme.CURRENT_SPACE;
                    pageTitle = page;
                }
            }
        }
        else{
            spaceKey = tablebasecme.CURRENT_SPACE;
            pageTitle = tablebasecme.CURRENT_PAGE;
        }
        
        $.extend(parms, {attSpace: spaceKey, attPage: pageTitle});
        
        return {
            icon: "/download/resources/org.swift.confluence.table/img/table-32x32.png",
            title: "Advanced Tables Editor - Attachment Table",
            showPreview: true,
            dataAttributes: {commontableeditor: "true", datalocationfields: "true"}, // required for all apps built around the common table editors for common event
            navigation: {
                primary: [
                    {
                        icon: appcme.absolutePath("/download/resources/org.swift.confluence.table/editor-img/icon-nav-attachment-48-wht-on-clr.png"),
                        name: "Attachment settings",
                        panel: org.swift.confluence.table.attachmenttable.editor.attachmentTableSettingsPanel(parms)
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
                        name: "Attachment Table guide",
                        url: "https://bobswift.atlassian.net/wiki/x/AoCAM" 
                    },
                    {
                        icon: appcme.absolutePath("/download/resources/org.swift.confluence.tablesorter/editor/img/icon-nav-docs-48-wht-on-clr.png"),
                        name: "Attachment Table Documentation",
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
