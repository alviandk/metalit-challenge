import Progress from "./container/ProgressChallenge";
import List from "./container/ListChallenge";
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
          <Route path="" component={List} exact />
          <Route path="/progress" component={Progress} exact />
        </Switch>
        <Footer />
      </div>
    </Router>
  );
}

export default App;