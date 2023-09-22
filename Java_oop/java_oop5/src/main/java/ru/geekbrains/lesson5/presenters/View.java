package ru.geekbrains.lesson5.presenters;

import ru.geekbrains.lesson5.models.Table;

import java.util.Collection;
import java.util.Date;

public interface View {

    /**
     * Отобразить список столиков в представлении
     * @param tables список столиков
     */
    void showTables(Collection<Table> tables);

    /**
     * Регистрация наблюдателя
     * @param observer
     */
    void setObserver(ViewObserver observer);

    /**
     * Распечатать результат бронирования столика
     * @param reservationNo
     */
    void printReservationTableResult(String name, int tableNo, Date oredrDate, int reservationNo);
}
