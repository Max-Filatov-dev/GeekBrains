package ru.geekbrains.lesson5.models;

import ru.geekbrains.lesson5.presenters.Model;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Date;
import java.util.Optional;

public class TableModel implements Model {

    private Collection<Table> tables;

    /**
     * Получить список всех столиков
     *
     * @return коллекция столиков
     */
    public Collection<Table> loadTables() {

        if (tables == null) {
            tables = new ArrayList<>();

            tables.add(new Table());
            tables.add(new Table());
            tables.add(new Table());
            tables.add(new Table());
            tables.add(new Table());
        }

        return tables;
    }


    /**
     * Бронирование столика
     *
     * @param reservationDate дата
     * @param tableNo         номер столика
     * @param name            имя клиента
     * @return номер брони
     */
    public int reservationTable(Date reservationDate, int tableNo, String name) {
        for (Table table : loadTables()) {
            if (table.getNo() == tableNo) {
                Reservation reservation = new Reservation(reservationDate, name);
                table.getReservations().add(reservation);
                table.setStatus(true);
                return reservation.getId();
            }
        }
        return -1;
        //throw new RuntimeException("Некорректный номер столика");
    }


    /**
     * TODO: Разработать самостоятельно
     * Поменять бронь столика
     *
     * @param oldReserv       номер старого резерва (для снятия)
     * @param reservationDate дата резерва столика
     * @param tableNo         номер столика
     * @param name            Имя
     */
    @Override
    public int changeReservationTable(int oldReserv, Date reservationDate, int tableNo, String name) {
        for (Table table : loadTables()) {
            if (table.isStatus()) {
                System.out.printf("Столик #%d уже забронирован! Выберите другой столик", tableNo);
//                Reservation reservation = new Reservation(reservationDate, name);
//                table.getReservations().add(reservation);
//                return reservation.getId();
            } else System.out.printf("\n%s, Ваша прежняя бронь №%d отменена!\n", name, 3);
        }
        return -1;
    }


}

