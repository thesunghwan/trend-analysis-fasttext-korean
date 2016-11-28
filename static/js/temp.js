$.getJSON('/static/result.json', function(data) {
    var json = {"countries_msg_vol": data};
    for(var prop in data) {
        data[prop] = data[prop] * data[prop] * data[prop] * data[prop] * data[prop];
    }
    draw(json);
});

$(".top-box input").keydown(function(e) {
    if (e.keyCode == 13) {
        var word = $(".top-box input").val();
        var spinner_container = $("<div id='spinner-container'></div>");
        $("body").append(spinner_container);
        var opts = {
          lines: 13 // The number of lines to draw
        , length: 28 // The length of each line
        , width: 14 // The line thickness
        , radius: 42 // The radius of the inner circle
        , scale: 1 // Scales overall size of the spinner
        , corners: 1 // Corner roundness (0..1)
        , color: '#000' // #rgb or #rrggbb or array of colors
        , opacity: 0.25 // Opacity of the lines
        , rotate: 0 // The rotation offset
        , direction: 1 // 1: clockwise, -1: counterclockwise
        , speed: 1 // Rounds per second
        , trail: 60 // Afterglow percentage
        , fps: 20 // Frames per second when using setTimeout() as a fallback for CSS
        , zIndex: 2e9 // The z-index (defaults to 2000000000)
        , className: 'spinner' // The CSS class to assign to the spinner
        , top: '50%' // Top position relative to parent
        , left: '50%' // Left position relative to parent
        , shadow: false // Whether to render a shadow
        , hwaccel: false // Whether to use hardware acceleration
        , position: 'absolute' // Element positioning
        }
        var target = document.getElementById('spinner-container');
        var spinner = new Spinner(opts).spin(target);

        $.ajax({
            url: "/list/" + word,
            type: "GET",
            success: function(resp) {
                var json = {"countries_msg_vol": resp};
                for(var prop in resp) {
                    resp[prop] = resp[prop] * resp[prop] * resp[prop] * resp[prop] * resp[prop];
                }
                draw(json);
                
                spinner_container.remove();
            }
        });
    }
});

var draw = function(raw_json) {
    $("#graph").children().remove();
    var diameter = 700;

    var svg = d3.select('#graph').append('svg')
    .attr('width', diameter)
    .attr('height', diameter);

    var bubble = d3.layout.pack()
    .size([diameter, diameter])
    .value(function(d) {return d.size;})
    .sort(function(a, b) {
        return -(a.value - b.value)
    })
    .padding(20);

    // generate data with calculated layout values
    var nodes = bubble.nodes(processData(raw_json))
    .filter(function(d) { return !d.children; }); // filter out the outer bubble

    var vis = svg.selectAll('circle')
    .data(nodes);

    vis.enter().append('circle')
    .attr('transform', function(d) { return 'translate(' + d.x + ',' + d.y + ')'; })
    .attr('r', function(d) { return d.r; })
    .attr('class', function(d) { return d.className; })
    .attr('fill', function(d) { return d.fill; });

    vis.enter().append("text")
    .attr('transform', function(d) { return 'translate(' + d.x + ',' + (d.y + 5) + ')'; })
    .text(function(d){return d.name})
    .attr('fill', 'white')
    .attr('font-size', '15px')
    .attr("text-anchor", "middle")
    .attr("font-weight", "bold")

    function processData(data) {
        var obj = data.countries_msg_vol;

        var newDataSet = [];
        var colors = ["#623722", "#b4835c", "#e1d8cd", "#bac1c8", "#342f30", "#aa6e47", "#d3d6da", "#836953"];



        for(var prop in obj) {
            var color = colors[Math.floor(Math.random()*colors.length)];
            newDataSet.push({name: prop, className: prop.toLowerCase(), fill: color, size: obj[prop]});
        }
        return {children: newDataSet};
    }
}

//draw();
//})();
