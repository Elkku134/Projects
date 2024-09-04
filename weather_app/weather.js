// Ilmatieteen laitoksen API URL. Tällä haetaan esimerkiksi lämpötila ja tuulen nopeus.
const apiUrl = 'https://opendata.fmi.fi/wfs?service=WFS&version=2.0.0&request=getFeature&storedquery_id=fmi::observations::weather::simple&place=Helsinki&parameters=temperature,windSpeed';



async function getWeatherData() {
    try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.text();
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(data, "text/xml");

        // Etsi lämpötila ja tuulen nopeus
        const temperatures = xmlDoc.getElementsByTagName("BsWfs:ParameterValue");
        const temperature = temperatures.length > 0 ? temperatures[0].textContent : 'Ei saatavilla';
        const windSpeeds = xmlDoc.getElementsByTagName("BsWfs:ParameterValue");
        const windSpeed = windSpeeds.length > 1 ? windSpeeds[1].textContent : 'Ei saatavilla';

        // Näytä tulokset sivulla
        document.getElementById('weather-info').innerHTML = `
            <p>Lämpötila: ${temperature} °C</p>
            <p>Tuulen nopeus: ${windSpeed} m/s</p>
        `;

    } catch (error) {
        console.error('Error fetching weather data:', error);
        document.getElementById('weather-info').textContent = "Tietojen haku epäonnistui.";
    }
}

getWeatherData();
