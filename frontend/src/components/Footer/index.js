import React, { Component } from "react";
import { Help, About, Contact, Term_Conditions, Privacy_Policy  } from '../../constant';

class Footer extends Component {
  render() {
    return (
      <footer className="bg-dark py-4 text-white px-3">
        <div className="footer-middle">
          <div className="container px-4 my-5">
            <div className="row mb-3">
              <div className="col-md-4 col-sm-6">
                <div className="footer-pad">
                  <ul className="list-unstyled px-4">
                    <li>
                      <a className="text-reset text-decoration-none" href={Help}>
                        Pusat Bantuan
                      </a>
                    </li>
                    <li>
                      <a className="text-reset text-decoration-none" href={About}>
                        Tentang Kami
                      </a>
                    </li>

                    <li>
                      <a className="text-reset text-decoration-none" href={Contact}>
                        Hubungi Kami
                      </a>
                    </li>

                    <li>
                      <a className="text-reset text-decoration-none" href={Term_Conditions}>
                        Syarat dan Ketentuan
                      </a>
                    </li>

                    <li>
                      <a className="text-reset text-decoration-none" href={Privacy_Policy}>
                        Kebijakan Privasi
                      </a>
                    </li>
                  </ul>
                </div>
              </div>
              <div className="col-md-4 col-sm-6"></div>
              <div className="col-md-3">
                <p className="px-3">Jl. Bangka Raya No.17, RT.13/RW.01, 
                    Bangka,Kec. Mampang Prpt, Kota Jakarta Selatan, 
                    Daerah Khusus Ibukota Jakarta 12730
                    <br/>Telp. 0857-7979-3635
                </p>
              </div>   
            </div>
            
            <div className="row">
              <div className="col-md-12 px-2">
                <p className="text-center px-3">
                  All Rights Reserved | Copyright © 2022 | PT Metamorfosa Teknologi Berdikari
                </p>
                <div className="text-center">
                  <span className="mx-2">
                    <a href="https://twitter.com/metalit_id" target="_blank">
                      <i className="fab fa-twitter"></i>
                    </a>
                  </span>
                  <span className="mx-2">
                    <a href="https://www.facebook.com/Metalit-107151784977073" target="_blank">
                      <i className="fab fa-facebook-f"></i>
                    </a>
                  </span>
                  <span className="mx-2">
                    <a href="https://instagram.com/metalit.id" target="_blank">
                      <i className="fab fa-instagram"></i>
                    </a>
                  </span>
                  <span className="mx-2">
                    <a href="https://www.linkedin.com/company/metalit-id" target="_blank">
                      <i className="fab fa-linkedin"></i>
                      </a>  
                  </span>  
                </div>
              </div>
            </div>
          </div>
        </div>
      </footer>
    )
  }
}

export default Footer;