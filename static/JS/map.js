var map = new AMap.Map("container", {
    mapStyle: 'amap://styles/macaron', //设置地图的显示样式
    resizeEnable: true,
    // center: [113.6770499, 23.3809537],
    // zoom: 4,
});

AMap.plugin('AMap.Geolocation', function () {
    var geolocation = new AMap.Geolocation({
        enableHighAccuracy: false, //是否使用高精度定位，默认:true 
        buttonPosition: 'RB', //定位按钮的停靠位置
        buttonOffset: new AMap.Pixel(10, 20), //定位按钮与设置的停靠位置的偏移量，默认：Pixel(10, 20)
        zoomToAccuracy: true, //定位成功后是否自动调整地图视野到定位点
    });
    map.addControl(geolocation);
    geolocation.getCurrentPosition();
    AMap.event.addListener(geolocation, 'complete', onComplete); //返回定位信息
    // AMap.event.addListener(geolocation, 'complete', onComplete);
    geolocation.getCurrentPosition(function (status, result) {
        if (status == 'complete') {
            onComplete(result)
        } else {
            // onError(result)
        }
    });
});





// // 获取用户所在城市信息
// function showCityInfo() {
//     //实例化城市查询类
//     var citysearch = new AMap.CitySearch();

//     //自动获取用户IP，返回当前城市
//     citysearch.getLocalCity(function (status, result) {
//         if (status === 'complete' && result.info === 'OK') {
//             if (result && result.city && result.bounds) {
//                 var cityinfo = result.city;
//                 var citybounds = result.bounds;
//                 document.getElementById('info').innerHTML = '您当前所在城市：' + cityinfo;
//                 //地图显示当前城市
//                 map.setBounds(citybounds);
//             }
//         } else {
//             document.getElementById('info').innerHTML = result.info;
//         }
//     });
// }

function onComplete(data) {
    document.getElementById('status').innerHTML = '定位成功'
    var mystr = [];
    mystr.push(data.position);
    var str = [];
    str.push('定位结果：' + data.position);
    str.push('定位类别：' + data.location_type);
    if (data.accuracy) {
        str.push('精度：' + data.accuracy + ' 米');
    } //如为IP精确定位结果则没有精度信息
    str.push('是否经过偏移：' + (data.isConverted ? '是' : '否'));
    document.getElementById('result').innerHTML = str.join('<br>');
    document.getElementById('textPosition').value = mystr;
    // document.getElementById('mytext').value = "aaaa";
    // customersForm.textPosition.value = 'data.position';
}
// showCityInfo();