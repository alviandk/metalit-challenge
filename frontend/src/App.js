import Task from "./container/Task";
import Challenge from "./container/Challenge";
import Payouts from "./container/Payouts";
import { BrowserRouter as Router, Switch, Route} from "react-router-dom";
import Navig from "./components/Navbar";
import Footer from "./components/Footer";
import './index.css';

function App() {
  return (
    <Router>
      <div className="App">
      	<Navig />
        <Switch>
          <Route path="/" component={Challenge} exact />
          <Route path="/task/:id" component={Task} exact />
          <Route path="/payouts" component={Payouts} exact />
        </Switch>
        <Footer />
      </div>
    </Router>
  );
}

export default App;