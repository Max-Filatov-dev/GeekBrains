package observer;

public class Master implements Observer {

    // region Private Fields

    private final String name;
    private final String vacancyWorker = "HR";

    private int salary = 100000;

    private String companyName;

    private boolean masterStatus = true;


    // endregion

    public Master(String name) {
        this.name = name;
    }

    // region Getters And Setters

    public String getVacancyWorker() {
        return vacancyWorker;
    }

    public String getName() {
        return name;
    }

    public boolean isWorkerStatus() {
        return masterStatus;
    }

    public int getSalary() {
        return salary;
    }

    public String getCompanyName() {
        return companyName;
    }

    // endregion

    @Override
    public void receiveOffer(String nameCompany, String companyVacancy, int salary) {
        if (this.salary <= salary && this.vacancyWorker.equals(companyVacancy)) {
            System.out.printf("Мастер %s %s: Мне нужна эта работа! (компания: %s, вакансия: %s, заработная плата: %d)\n",
                    vacancyWorker, name, nameCompany, companyVacancy, salary);
            this.salary = salary;
            companyName = nameCompany;
            masterStatus = false;
        } else {
            System.out.printf("Мастер %s %s: Я найду работу получше! (компания: %s, вакансия: %s, заработная плата: %d)\n",
                    vacancyWorker, name, nameCompany, companyVacancy, salary);
        }
    }


}
