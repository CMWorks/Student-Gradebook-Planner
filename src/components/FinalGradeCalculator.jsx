import React from "react";
import Popup from "./Popup";

class FinalGradeCalculator extends React.Component
{
    constructor(props) {
        super(props);
        this.state = {
            curGrade: 0,
            desiredGrade: 0,
            finalWeight: 0,
            gradeNeeded: 0,
            popUpFinalGrade: false,
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        const value = +event.target.value;
        const name = event.target.name;

        this.setState({[name]: value});
    }

    handleSubmit(event) {
        const curGrade = this.state.curGrade;
        const desiredGrade = this.state.desiredGrade;
        const finalWeight = this.state.finalWeight / 100;
        let localGradeNeeded = ( desiredGrade  -  curGrade * (1-finalWeight) )  /  finalWeight;
        this.setState({gradeNeeded: localGradeNeeded});
        // alert('curGrade = ' + curGrade + '\ndesiredGrade = ' + desiredGrade + '\nfinalWeight = ' + finalWeight + "\ngradeNeeded = " + gradeNeeded);
        this.setState({popUpFinalGrade: true});
        event.preventDefault();
    }

    render() {
        return (
        <div>
            <div className="container">
                <Popup trigger={this.state.popUpFinalGrade}>
                    <h3>Result:</h3>
                    <div>
                        <label>You need a {this.state.gradeNeeded}% on your final in order to get a {this.state.desiredGrade}% overall.</label>
                    </div>
                    <button className="btn btn-primary" onClick={() => this.setState({ popUpFinalGrade: false })}> Okay </button>
                </Popup>

                {/* Input for current grade. */}
                <form>
                    <label>
                        Current grade is
                        <input name="curGrade" type="number" value={this.state.curGrade} onChange={this.handleChange} />
                        %.
                    </label>
                </form>

                {/* Input for desired grade. */}
                <form>
                    <label>
                        I want a 
                        <input name="desiredGrade" type="number" value={this.state.desiredGrade} onChange={this.handleChange} />
                        % in the class.
                    </label>
                </form>

                {/* Input for exam weight. */}
                <form>
                    <label>
                        Final is worth 
                        <input name="finalWeight" type="number" value={this.state.finalWeight} onChange={this.handleChange} />
                        % of total grade.
                    </label>
                </form>

                {/* Submit */}
                <form name="submit" onSubmit={this.handleSubmit}>
                    <input type="submit" value="Calculate Answer" />
                </form>
            </div>
        </div>
        )
    }
}

export default FinalGradeCalculator;