<%include file="header.mako"/>
<%include file="search_boxes.mako"/>
<script type="text/javascript" src="${db.locals['db_url']}/js/bibliography.js"></script>
<div class='philologic_response'>
    <div class='initial_report'>
        <p class='description'>Bibliography Report: ${len(results)} results.</p>
        <%include file="show_frequency.mako"/>
    </div>
    <div class="results_container">
        <div class='bibliographic_results'>
            <ol class='philologic_cite_list'>
            % for i in results:
             <li class='philologic_occurrence'>
             ##  <input type="checkbox" name="philo_id" value="${i.philo_id}">
             % if i.type == 'doc':
             <span class='philologic_cite'>${f.cite.make_abs_doc_cite(db,i)} <b>Volume ${i.volume}</b></span>
             % else:
             <span class='philologic_cite'>${f.cite.make_abs_div_cite(db,i)}</span>
             % endif
             </li>
            % endfor
            </ol>
       </div>
   </div>
</div>
<%include file="footer.mako"/>
