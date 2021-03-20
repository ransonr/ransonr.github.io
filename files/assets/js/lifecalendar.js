(function(){

  function dateToString(d) {
    var year = d.getUTCFullYear();
    var month = d.getUTCMonth() + 1;
    var day = d.getUTCDate();
    return year + "-" + (month < 10 ? "0" + month : month) + "-" + (day < 10 ? "0" + day : day);
  }

  function addDaysToDate(d, days) {
    return new Date(d.getUTCFullYear(), d.getUTCMonth(), d.getUTCDate() + days);
  }

  function addYearsToDate(d, years) {
    return new Date(d.getUTCFullYear() + years, d.getUTCMonth(), d.getUTCDate());
  }

  function ageString(years, weeks) {
    return years + " year" + (years === 1 ? " " : "s ") + weeks + " week" + (weeks === 1 ? "" : "s");
  }

  function hoverText(d) {
    var text = "<table class='table table-condensed table-bordered'>";
    text += "<tr><td>Date:</td><td>" + dateToString(d.beginDate) + "</td></tr>";
    text += "<tr><td>Week:</td><td>" + d.week + "</td></tr>";
    text += "<tr><td>Age:</td><td>" + d.age + "</td></tr>";
    text += "</table>";
    return text;
  }

  function gridData() {
    var data = new Array();
    var xpos = 1; //starting xpos and ypos at 1 so the stroke will show when we make the grid below
    var ypos = 1;
    var width = 12;
    var height = 12;
    var yearCount = 0;
    var today = new Date();
    var birthDate = new Date(document.getElementById("birthdate-input").value);
    var weekStart = new Date(birthDate.getTime());

    for (var row = 0; row < 100; row++) {
      data.push( new Array() );

      for (var column = 0; column < 52; column++) {
        data[row].push({
          x: xpos,
          y: ypos,
          width: width,
          height: height,
          fill: weekStart < today ? "#b0c4d3" : "#fff",
          week: row * 52 + column,
          age: ageString(yearCount, column),
          beginDate: weekStart,
        })

        xpos += width;
        weekStart = addDaysToDate(weekStart, 7);
      }

      xpos = 1;
      ypos += height;
      weekStart = addYearsToDate(birthDate, ++yearCount);
    }

    return data;
  }

  function drawCalendar() {
    var calData = gridData();

    var grid = d3.select("#grid")
      .append("svg")
      .attr("width", "800px")
      .attr("height", "1400px");

    var row = grid.selectAll(".row")
      .data(calData)
      .enter().append("g")
      .attr("class", "row");

    var column = row.selectAll(".square")
      .data(function(d) { return d; })
      .enter().append("rect")
      .attr("class", "square")
      .attr("x", function(d) { return d.x; })
      .attr("y", function(d) { return d.y; })
      .attr("width", function(d) { return d.width; })
      .attr("height", function(d) { return d.height; })
      .style("fill", function(d) { return d.fill; })
      .style("stroke", "#222")
      .on('mouseover', function(d) {
        d3.select(this).style("fill", "#4169e1");
        tooltip.html(hoverText(d));
        tooltip.style("visibility", "visible");
      })
      .on('mousemove', function() {
        tooltip
          .style("top", (d3.event.pageY - 15) + "px")
          .style("left", (d3.event.pageX + 15) + "px");
      })
      .on('mouseout', function(d) {
        d3.select(this).style("fill", d.fill);
        tooltip.style("visibility", "hidden");
      });
  }

  var tooltip = d3.select("body")
    .append("div")
    .attr("id", "tooltip")
    .attr("class", "panel text-info small")
    .style("position", "absolute")
    .style("z-index", "10")
    .style("visibility", "hidden");

  drawCalendar();

  $(document).ready(function(){
    $('input[type="date"]').change(function(){
      d3.select("#grid").selectAll("*").remove();
      drawCalendar();
    });
  });

})();
