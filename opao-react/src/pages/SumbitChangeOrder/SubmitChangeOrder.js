import Navigation07LeftNavigation2 from "../components/Navigation07LeftNavigation2";
import styles from "./SubmitChangeOrder.module.css";

const SubmitChangeOrder = () => {
  return (
    <div className={styles.submitChangeOrder}>
      <Navigation07LeftNavigation2 />
      <div className={styles.frameWithText}>
        <h2 className={styles.addProduct}>Submit Change Order</h2>
      </div>
      <header className={styles.navigation08TopNavigation0} />
    </div>
  );
};

export default SubmitChangeOrder;
