import React from 'react';
import Riley from '../assets/img/riley_headshot.jpg';
import Faith from '../assets/img/faith_headshot.jpg';
import Max from '../assets/img/max_headshot.jpg';

const About = () => {
    return (
        <>
        <h1 style={{marginLeft: "10px"}}>
            About Us
        </h1>
        <h5 style={{marginLeft: "10px"}}>
            Our product utilizes a split-flap design in order to
            display the best and shortest train route to take.
        </h5>
        <br></br>
        <h2 style={{marginLeft: "10px"}}>
            Meet the team
        </h2>
        <br></br>
        <div class="members-container">
            <div className="left">
                <div class="profile">
                    <h2>Riley Dou</h2>
                    <div class="title title--epic">Head of Programming</div>
                    <div class="desc">Riley is majoring in Math & CS at NYU Tandon. She participated in HackNYU 2023!</div>
                    <br></br>
                    <img src={Riley} alt="Riley"></img>
                    <br></br>
                    <a href="https://github.com/rilieo">Github</a>
                    <br></br>
                </div>
            </div>
            <div className="center">
                <div class="profile">
                    <h2>Maximilian Ta</h2>
                    <div class="title title--legendary">Head of Back-End Dev</div>
                    <div class="desc">Max is pursuing a CS major at NYU Tandon. He was a former lead QA at Area28!</div>
                    <br></br>
                    <img src={Max} alt="Max"></img>
                    <br></br>
                    <a href="https://github.com/Flooflez">Github</a>
                    <br></br>
                </div>
            </div>
            <div className="right">
                <div class="profile">
                    <h2>Faith Villarreal</h2>
                    <div class="title title--common">Head of Mechanical Design</div>
                    <div class="desc">Faith is pursuing a CS Major at NYU Tandon. She is a community service activist!</div>
                    <br></br>
                    <img src={Faith} alt="Faith"></img>
                    <br></br>
                    <a href="https://github.com/faithvillarr">Github</a>
                    <br></br>
                </div>
            </div>
        </div>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        </>
    )
}

export default About;