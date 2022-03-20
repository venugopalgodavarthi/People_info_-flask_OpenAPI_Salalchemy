/*
 * JavaScript file for the application to demonstrate
 * using the API
 */

// Create the namespace instance
let ns = {};

// Create the model instance
ns.model = (function() {
    'use strict';

    let $event_pump = $('body');

    // Return the API
    return {
        'read': function() {
            let ajax_options = {
                type: 'GET',
                url: '/people',
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_read_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        create: function(pid,name,ptype,age,desc,date,check) {
            let ajax_options = {
                type: 'POST',
                url: '/people',
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'pid': parseInt(pid),
                    'name': name,
                    'ptype': ptype,
                    'age': parseInt(age),
                    'desc': desc,
                    'date': date,
                    'check': check
                })
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_create_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        update: function(pid,name,ptype,age,desc,date,check) {
            let ajax_options = {
                type: 'PUT',
                url: '/people/' + pid,
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'pid': parseInt(pid),
                    'name': name,
                    'ptype': ptype,
                    'age': age,
                    'desc': desc,
                    'date':date,
                    'check':check
                })
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_update_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        'delete': function(pid) {
            let ajax_options = {
                type: 'DELETE',
                url: '/people/' + pid,
                accepts: 'application/json',
                contentType: 'plain/text'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_delete_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        }
    };
}());

// Create the view instance
ns.view = (function() {
    'use strict';

    let $pid = $('#pid'),
    $name = $('#name'),
    $ptype = $('#ptype'),
    $age = $('#age'),
    $check=$('#check'),
    $desc = $('#desc');

    // return the API
    return {
        reset: function() {
            $pid.val('').focus();
            $name.val('').focus();
            $ptype.val('').focus();
            $age.val('').focus();
            $desc.val('').focus();
            $check.val('').focus();
        },
        update_editor: function(pid,name,ptype,age,desc,date,check) {
            $pid.val(pid).focus();
            $name.val(name).focus();
            $ptype.val(ptype).focus();
            $age.val(age).focus();
            $desc.val(desc).focus();
            $date.val(date).focus();
            $check.val(check).focus();
        },
        build_table: function(people) {
            let rows = ''

            // clear the table
            $('.people table > tbody').empty();

            // did we get a people array?
            if (people) {
                for (let i=0, l=people.length; i < l; i++) {
                    rows += `<tr><td class="id">${people[i].pid}</td>
                    <td class="name">${people[i].name}</td>
                    <td class="ptype">${people[i].ptype}</td>
                    <td class="age">${people[i].age}</td>
                    <td class="desc">${people[i].desc}</td>
                    <td>${people[i].date}</td>
                    <td ><a href='/update/${people[i].pid}/'>update</a></td>
                    <td ><a href='/delete/${people[i].pid}/'>delete</a></td>
                    </tr>`;
                }
                $('table > tbody').append(rows);
            }
        },
        error: function(error_msg) {
            $('.error')
                .text(error_msg)
                .css('visibility', 'visible');
            setTimeout(function() {
                $('.error').css('visibility', 'hidden');
            }, 3000)
        }
    };
}());

// Create the controller
ns.controller = (function(m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body'),
        $pid = $('#pid'),
        $name = $('#name'),
        $ptype = $('#ptype'),
        $age = $('#age'),
        $desc = $('#desc'),
        $date = $('#date'),
        $check= $('#check');

    // Get the data from the model after the controller is done initializing
    setTimeout(function() {
        model.read();
    }, 100)

    // Validate input
    function validate(pid, name,ptype,age,desc,date,check) {
        return pid !== "" && name !== "" && ptype !== "" && age !== "" && date !== "" && desc !== "" && check !== "";
    }

    // Create our event handlers
    $('#create').click(function(e) {
        let pid = $pid.val(),
                    name= $name.val(),
                    ptype= $ptype.val(),
                    age = $age.val(),
                    desc = $desc.val();
                    date = $date.val();
                    check = $check.val();

        e.preventDefault();

        if (validate(pid, name,ptype,age,desc,date,check)) {
            model.create(pid, name,ptype,age,desc,date, check)
        } else {
            alert('Problem with first or last name input');
        }
    });

    $('#update').click(function(e) {
        let pid = $pid.val(),
         name = $name.val(),
         ptype = $ptype.val(),
         age = $age.val(),
         date = $date.val(),
         check = $check.val(),
         desc = $desc.val();

        e.preventDefault();

        if (validate(pid,name,ptype,age,date,check,desc)) {
            model.update(pid,name,ptype,age,date,check,desc)
        } else {
            alert('Problem with pid,name,ptype,age,desc input');
        }
        e.preventDefault();
    });

    $('#delete').click(function(e) {
        let pid = $pid.val();

        e.preventDefault();

        if (validate('placeholder', pid)) {
            model.delete(pid)
        } else {
            alert('Problem with id,name,ptype,age,desc input');
        }
        e.preventDefault();
    });

    $('#reset').click(function() {
        view.reset();
    })

    $('table > tbody').on('dblclick', 'tr', function(e) {
        let $target = $(e.target),
            pid,
            name,
            ptype,
            age,
            desc,
            date,
            check;

        pid = $target
            .parent()
            .find('td.pid')
            .number();

        name = $target
            .parent()
            .find('td.name')
            .text();

          ptype = $target
            .parent()
            .find('td.ptype')
            .text();
          
          age = $target
            .parent()
            .find('td.age')
            .text();
          desc = $target
            .parent()
            .find('td.desc')
            .text();
            date = $target
            .parent()
            .find('td.date')
            .text();
          check = $target
            .parent()
            .find('td.check')
            .text();

        view.update_editor(pid,name,ptype,age,desc,date,check);
    });

    // Handle the model events
    $event_pump.on('model_read_success', function(e, data) {
        view.build_table(data);
        view.reset();
    });

    $event_pump.on('model_create_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_update_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_delete_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_error', function(e, xhr, textStatus, errorThrown) {
        let error_msg = textStatus + ': ' + errorThrown + ' - ' + xhr.responseJSON.detail;
        view.error(error_msg);
        console.log(error_msg);
    })
}(ns.model, ns.view));

