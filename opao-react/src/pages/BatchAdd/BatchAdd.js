import Navigation07LeftNavigation from "../components/Navigation07LeftNavigation";
import styles from "./Addbatch.module.css";

const Addbatch = () => {
  return (
    <div className={styles.addbatch}>
      <h2 className={styles.orders}>
        <p className={styles.addToBatch}>Add To Batch</p>
      </h2>
      <main className={styles.orders1} />
      <header className={styles.navigation08TopNavigation0} />
      <Navigation07LeftNavigation />
    </div>
  );
};

export default Addbatch;
