<?php
// 파이 차트 생성에 필요한 데이터
$data = array(
  array('Task', 'Hours per Day'),
  array('Work', 8),
  array('Eat', 2),
  array('Sleep', 8),
  array('Exercise', 2)
);

// 데이터를 JSON 형식으로 변환
$json_data = json_encode($data);

// 구글 차트 API 호출
$url = 'https://chart.googleapis.com/chart?cht=p&chd=t:' . $json_data . '&chs=250x100';
?>

<!-- 파이 차트를 표시할 DOM 요소 -->
<div id="chart-container"></div>

<!-- jQuery를 사용하여 Ajax 요청 보내기 -->
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
  // 1초마다 데이터 업데이트
  setInterval(function() {
    $.ajax({
      url: 'get_data.php', // 실시간 데이터를 반환하는 PHP 파일 경로
      dataType: 'json',
      success: function(data) {
        // 파이 차트 업데이트
        var chart_data = google.visualization.arrayToDataTable(data);
        var chart_options = {title: 'My Daily Activities', is3D: true};
        var chart = new google.visualization.PieChart(document.getElementById('chart-container'));
        chart.draw(chart_data, chart_options);
      }
    });
  }, 1000);
</script>

<!-- 클라이언트 측 JavaScript에서 파이 차트 생성 -->
<script>
  var chart_url = "<?php echo $url; ?>";
  var img = document.createElement("img");
  img.src = chart_url;
  document.body.appendChild(img);
</script>
