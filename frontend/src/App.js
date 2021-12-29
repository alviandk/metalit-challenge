import Coba from "./container/ProgressChallenge";
import Progress from "./components/Coba";
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
          <Route path="/" component={Coba} exact />
          <Route path="/a" component={Progress} exact />
        </Switch>
        <Footer />
      </div>
    </Router>
  );
}

export default App;