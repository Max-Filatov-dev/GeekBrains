package homework;

import homework.moex.GetTickerDataMoex;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        ArrayList<String> tickers = new ArrayList<>();
        tickers.add("sber");
        tickers.add("phor");
        tickers.add("upro");

        GetTickerDataMoex getDataMoex = new GetTickerDataMoex();
        tickers.forEach(getDataMoex::getTickerDataMoex);

    }

}
