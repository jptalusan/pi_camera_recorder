$(document).ready(function() {
    // var socket = io.connect('http://' + document.domain + ':' + location.port);
    
    // socket.on('connect', function() {
    //     console.log('client_connected')
    //     socket.emit('client_connected', {data: 'new client!'});
    // });

    // socket.on('my event', function(data) {
    //     console.log('message to backend');
    //     socket.emit('my event', {hello: 'world'})
    // });

    $("#record_button").on("click", function() {
        var buttonText = $(this).text();
        console.log(buttonText);
        console.log("clicked!");
        // socket.emit('my_event', {data: 'record button is clicked'});
        // socket.emit('record_event', {curr_flag_state : 'False'});
        // socket.emit('my event', '{"data":"Hello fool!"}');


    });



    window.setInterval(yourfunction, 5000);

    function yourfunction() { 
        $.getJSON('http://163.221.68.237:5000/pi_photos', function(data) {
            $("#toptitle").text(data.path);
        });
    }


    // $("#jsonbutton").on("click", function() {
    //     alert("Hello!");
    //     console.log('message to backend');
    //     socket.emit('my event', '{"data":"HELLO FOOL~!!!!"}');
    // });

    // $("#jsonbutton").click(function() {
    //     alert("Hello!");
    //     console.log('message to backend');
    //     socket.emit('my event', '{"data":"HELLO FOOL~!!!!"}');
    //     // socket.send('{"message": "test"}');
    // });

    // socket.on('record_response', function(data) {
    //     console.log('received record response.')
    //     console.log(data)
    //     next_flag_state = data['next_flag_state']
    //     console.log(next_flag_state);
    //     if(next_flag_state == 'True') {
    //         $("#jsonbutton").prop('value', 'Recording...')
    //     } else {
    //         $("#jsonbutton").prop('value', 'Record')
    //     }
    // });

    // socket.on('test', function(data) {
    //     console.log(data);
    //     console.log('received test');
    // });

    // socket.on('my_response', function(data) {
    //     console.log('message from backend ');
    //     console.log(data)
    // });



});
