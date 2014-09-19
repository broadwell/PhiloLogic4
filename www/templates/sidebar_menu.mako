<div class="btn-group pull-right">
    <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">
        Display frequency by
        <span id="selected-sidebar-option" data-selected="${config['facets'][0]}">
            <%
            try:
                default_value = config["metadata_aliases"][config["facets"][0]].title()
            except KeyError:
                default_value = config['facets'][0].title()
            %>
            ${default_value}
        </span>
        <span class="caret"></span>
    </button>
    <ul class="dropdown-menu" role="menu" id="frequency_field">
        % for facet in config["facets"]:
            <%
            if facet in config["metadata_aliases"]:
                alias = config["metadata_aliases"][facet]
            else:
                alias = facet
            %>
            <li><a class="sidebar-option" id="side_opt_${facet}" data-value='${facet}' data-display='${facet}'>Display frequency by ${alias}</a></li>
        % endfor
        % if report != 'bibliography':
            <li class="divider"></li>
            <li><a class="sidebar-option" id="side_opt_collocate" data-value='collocation_report' data-display='collocate'>Display collocates</a></li>
        % endif
    </ul>
    <button type="button" id="hide-sidebar-button" class="btn btn-primary" style="display: none";>
        <span class="glyphicon glyphicon-remove-circle" style="vertical-align: text-top"></span>
    </button>
</div>