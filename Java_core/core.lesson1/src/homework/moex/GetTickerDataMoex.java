package homework.moex;

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URL;


public class GetTickerDataMoex {

    public void getTickerDataMoex(String ticker) {

        String urlMoex = "https://iss.moex.com/iss/";
        String urlEnginesRus = "engines/stock/markets/shares/boards/tqbr/securities/";
        String params = "?iss.meta=off&group_by=type&securities" +
                ".columns=SECID%2CSHORTNAME%2CISIN%2CPREVPRICE%2CPREVDATE&marketdata" +
                ".columns=LAST%2CCHANGE%2CLASTTOPREVPRICE%2CUPDATETIME%2CSYSTIME";
        String urlTickerRus = urlMoex + urlEnginesRus + ticker + "/.json" + params;
        String inputLine;

        try {
            var url = URI.create(urlTickerRus).toURL();
            BufferedReader in = getBufferedReader(url);
            StringBuilder response = new StringBuilder();
            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();

            JsonObject jsonObj = JsonParser.parseString(response.toString()).getAsJsonObject();
            JsonArray securitiesData =
                    jsonObj.getAsJsonObject("securities").getAsJsonArray("data").get(0).getAsJsonArray();

            System.out.printf("Ticker: %s Name: %s Last price: %s %n",
                    securitiesData.get(0),
                    securitiesData.get(1),
                    securitiesData.get(3));

        } catch (IOException err) {
            err.printStackTrace();
        }

    }

    private static BufferedReader getBufferedReader(URL url) throws IOException {
        HttpURLConnection connect = (HttpURLConnection) url.openConnection();
        connect.setRequestMethod("GET");
        connect.setRequestProperty("User-Agent",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15");
        return new BufferedReader(new InputStreamReader(connect.getInputStream()));
    }

}
