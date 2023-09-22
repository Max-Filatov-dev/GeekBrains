package ru.geekbrains.lesson5.views;

import ru.geekbrains.lesson5.models.Table;
import ru.geekbrains.lesson5.presenters.View;
import ru.geekbrains.lesson5.presenters.ViewObserver;

import java.util.Collection;
import java.util.Date;

public class BookingView implements View {

    private ViewObserver observer;

    public void showTables(Collection<Table> tables) {
        for (Table table : tables) {
//            System.out.println(table + " " + table.isStatus());
            System.out.printf("%s %s\n", table, table.isStatus());
        }
    }

    @Override
    public void setObserver(ViewObserver observer) {
        this.observer = observer;
    }

    @Override
    public void printReservationTableResult(String name, int tableNo, Date date, int reservationNo) {
        if (reservationNo > 0)
            System.out.printf("\n%s, столик #%d успешно забронирован %s. Номер вашей брони: #%d\n", name, tableNo, date, reservationNo);
        else
            System.out.printf("\n%s, не удалось забронировать столик #%d. Попробуйте выполнить операцию позже.", name, reservationNo);
    }

    public void reservationTable(Date orderDate, int tableNo, String name) {
        observer.onReservationTable(orderDate, tableNo, name);
    }

    /**
     * Действие клиента (пользователь нажал на кнопку отмены бронирования)
     *
     * @param oldReservation  идентификатор бронирования (старый)
     * @param reservationDate дата бронирования
     * @param tableNo         номер столика
     * @param name            Имя
     */
    public void changeReservationTable(int oldReservation, Date reservationDate, int tableNo, String name) {
        //TODO: Реализовать самостоятельно в рамках домашней работы
//        System.out.printf("\n%s, Ваша прежняя бронь №%d отменена!\n", name, oldReservation);
        observer.chReservationTable(oldReservation, reservationDate, tableNo, name);
    }

}
