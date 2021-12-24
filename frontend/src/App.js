import Coba from "./components/Coba";
import { BrowserRouter as Router, Switch, Route} from "react-router-dom";
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/" component={Coba} exact />
        </Switch>
      </div>
    </Router>
  );
}

export default App;