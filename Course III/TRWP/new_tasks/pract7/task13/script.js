class Hospital {
    constructor(name, lat, lon, address, area) {
        this.name = name;
        this.lat = lat;
        this.lon = lon;
        this.address = address;
        this.area = area
    }

    showInfo() {
        return "<b>" + this.name + "</b><br>" + this.address
    }

}

async function dataInit() {
    let url = 'http://localhost:63342/data.json';
    let data = await (await fetch(url)).json();

    let hospitalArray = [];
    for (let i = 0; i < data.length; i++) {

        let name = data[i]["ShortName"];

        for (let j = 0; j < data[i]["geoData"]["coordinates"].length; j++) {
            let coords = data[i]["geoData"]["coordinates"][j];
            let address = data[i]["ObjectAddress"][j]["Address"];
            let area = data[i]["ObjectAddress"][j]["AdmArea"]
            let hospital = new Hospital(name, coords[1], coords[0], address, area)
            hospitalArray.push(hospital);
        }
    }

    return hospitalArray;
}

async function statsCounter(dataArray) {

    let stat = new Map();

    for (let i = 0; i < dataArray.length; i++) {
        let area = dataArray[i].area;
        if (area === undefined) {
            continue
        }

        if (stat.has(area) === false) {
            stat.set(area, 0);
        }

        //Да, это такой инкремент
        stat.set(area, stat.get(area) + 1);
    }

    return new Map([...stat.entries()].sort((a, b) => b[1] - a[1]));
}

async function tableStats() {

    let hospitalArray = await dataInit();

    let stats = await statsCounter(hospitalArray);

    let returnStr = '<table class="table"><thead><tr><th scope="col">№</th><th scope="col">Округ</th><th scope="col">Кол-во больниц</th></tr></thead><tbody>'
    let bufferCounter = 1;
    for (let [key, value] of stats) {
        returnStr += '<tr> <th scope="row">' + bufferCounter + '</th><td>' + key + '</td> <td>' + value + '</td></tr>';
        bufferCounter++;
    }
    returnStr += ' </tbody></table>'
    document.getElementById("mytable").innerHTML = returnStr;
}


async function dataFiller() {
    let hospitalArray = await dataInit();

    let map = L.map('map').setView({lat: 55.75343329146573, lon: 37.61715415648654}, 8.5);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19, attribution: '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap contributors</a>'
    }).addTo(map);

    L.control.scale().addTo(map);

    for (let i = 0; i < hospitalArray.length; i++) {
        L.marker({
            lon: hospitalArray[i].lon,
            lat: hospitalArray[i].lat
        }).bindPopup(hospitalArray[i].showInfo()).addTo(map);
    }

}

async function randomGen() {
    let point = {}
    point.lat = (Math.random() * (55.84 - 55.63) + 55.63)
    point.lon = (Math.random() * (37.38 - 37.82) + 37.82)
    return point
}

async function getMainPoints(pointsArray) {

    let resultArray = Array()

    let sortedArr = pointsArray.sort(function (a, b) {
        return a.lon - b.lon;
    });

    resultArray.push([sortedArr[0].lat, sortedArr[0].lon]);
    resultArray.push([sortedArr[1].lat, sortedArr[1].lon]);
    return resultArray
}


async function randomFiller() {

    let map = L.map('map').setView({lat: 55.75343329146573, lon: 37.61715415648654}, 8.5);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19, attribution: '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap contributors</a>'
    }).addTo(map);

    L.control.scale().addTo(map);

    let pointsArray = Array()
    for (let i = 0; i < 25; i++) {
        let point = await randomGen();
        L.marker({lon: point.lon, lat: point.lat}).addTo(map);
        pointsArray.push(point);
    }

    let polylinePoints = await getMainPoints(pointsArray);
    let polyline = L.polyline(polylinePoints).addTo(map);

    for (let i = 0; i < 10; i++) {
        point = await randomGen();
        L.marker({lon: point.lon, lat: point.lat}).addTo(map);
    }

}